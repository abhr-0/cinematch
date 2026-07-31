# CineMatch

A Simple content-based movie recommender trained from TMDB data and built with Streamlit UI.

Data Source: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Deployed App: [https://cinematch-abhr-0.streamlit.app](https://cinematch-abhr-0.streamlit.app)

## Requirements
- nix (recommended)
or
- uv
or
- devcontainers
or
- Python (>=3.13) + pip (>=25.1)

## Quickstart

1. Clone the repository:
```sh
git clone https://github.com/abhr-0/cinematch
```

2. Setup the environment:

For nix:\
If your system has nix-direnv, just run `direnv allow` in the project root, otherwise,
use `nix develop` command to enter a devshell.

For uv:
```sh
uv sync --locked
```

For pip:
```sh
python3 -m venv .venv
source .venv/bin/activate # for Linux/Mac, for Windows: `.venv\Scripts\activate`
pip install -e . --group dev
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