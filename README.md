# Movie Recommender System

Simple content-based movie recommender built from TMDB data with Streamlit UI.

Data Source: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## Requirements
- Python 3.13
- See `requirements.txt`

## Quickstart

1. Clone the repository:
```sh
git clone https://github.com/abhr-0/movie_recommender_system
```

2. Install dependencies or use `nix develop`:
```sh
pip install -r requirements.txt
```

3. Set TMDB API key (create `.env` or export env var):
```env
TMDB_API_KEY=your_api_key_here
```

4. Run the Streamlit app:
```sh
streamlit run app/app.py
```

