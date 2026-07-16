# CineMatch

A Simple content-based movie recommender trained from TMDB data and built with Streamlit UI.

Data Source: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Deployed App: [https://cinematch-abhr-0.streamlit.app](https://cinematch-abhr-0.streamlit.app)

## Requirements
- Python 3.13
- See `requirements.txt`

## Quickstart

1. Clone the repository:
```sh
git clone https://github.com/abhr-0/cinematch
```

2. Install dependencies or use `nix develop`:
```sh
pip install -r requirements.txt
```

3. Set TMDB Bearer Token in `.streamlit/secrets.toml`:
```toml
TMDB_BEARER_TOKEN = "your_bearer_token_here"
```

4. Run the Streamlit app:
```sh
streamlit run app/app.py
```

## Docker (or, Podman)

1. Build the Docker image:
```sh
docker build -t cinematch .
```

2. Run the container:
```sh
docker run -p 8501:8501 -v=.streamlit/secrets.toml:/app/.streamlit/secrets.toml:ro cinematch
```