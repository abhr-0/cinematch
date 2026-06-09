import streamlit as st
import pandas as pd
import pickle
import requests
from dotenv import load_dotenv
import os
from math import exp

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

movies_dict = pickle.load(open("app/movies_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("app/similarity.pkl", "rb"))

st.title("Movie Recommender System")

selected = st.selectbox("Enter movie name:", movies["title"].values)

def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}")
    data = response.json()
    # st.text(data)
    return "https://images.tmdb.org/t/p/w500" + data["poster_path"]

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_posters = []
    similarity_scores = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        similarity_scores.append(i[1])
    
    return recommended_movies, recommended_posters, similarity_scores

def scale_scores(scores):
    return [int(100 / (1 + exp(-12*(score - 0.20)))) for score in scores]

if st.button("Recommend"):
    recommendations, posters, raw_scores = recommend(selected)

    scaled_scores = scale_scores(raw_scores)

    for i in range(5):
        col1, col2 = st.columns([1, 3])
        col1.image(posters[i])
        with col2.container(vertical_alignment="distribute"):
            st.header(recommendations[i], anchor=False, divider="gray")
            st.progress(scaled_scores[i], text=f"Similarity: {int(scaled_scores[i])}%")
