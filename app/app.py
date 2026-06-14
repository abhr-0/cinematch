import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import requests
from dotenv import load_dotenv
import os
from math import exp

@st.cache_resource
def load_movies_and_embeddings():
    movies_dict = pickle.load(open("app/movies_dict.pkl", "rb"))
    movies = pd.DataFrame(movies_dict)

    embeddings = pickle.load(open("app/embeddings.pkl", "rb"))
    return movies, embeddings

@st.cache_data(show_spinner=False)
def fetch_poster(poster_path):
    return requests.get("https://images.tmdb.org/t/p/w500" + poster_path).content

@st.cache_data(show_spinner=False)
def fetch_movie_details(movie_id):
    return requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}").json()

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    similarities = cosine_similarity(embeddings[movie_index], embeddings).flatten()

    movies_list = sorted(list(enumerate(similarities)), reverse=True, key= lambda x: x[1])[1:6]

    for i in movies_list:
        movie_details = fetch_movie_details(movies.iloc[i[0]].movie_id)
        yield {
            "title": movies.iloc[i[0]].title,
            "poster_path": movie_details["poster_path"],
            "overview": movie_details["overview"],
            "score": i[1]
        }

def scale_score(score):
    return int(100 / (1 + exp(-12*(score - 0.20)))) 

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

movies, embeddings = load_movies_and_embeddings()

st.title("CineMatch")
st.caption("A Content-Based Movie Recommender")

with st.container(horizontal=True, vertical_alignment="bottom"):
    selected = st.selectbox("Enter movie name:", movies["title"].values)
    recommend_button_press = st.button("Recommend")

if recommend_button_press:
    rows = [st.empty() for _ in range(5)]

    for row, recommendation in zip(rows, recommend(selected)):
        # Pre-fetch to not display an empty container with borders while app is waiting for poster
        fetched_poster = fetch_poster(recommendation["poster_path"])

        with row.container(border=True):
            col1, col2 = st.columns([1, 3])
            col1.image(fetched_poster)

            with col2.container():
                scaled_score = scale_score(recommendation["score"])

                st.subheader(recommendation["title"], anchor=False)
                st.text(recommendation["overview"])
                st.progress(scaled_score, text=f"Similarity: {int(scaled_score)}%")
