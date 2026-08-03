import pandas as pd

# Load The Movie Dataset
movies = pd.read_csv("dataset/tmdb_5000_movies.csv")
credits = pd.read_csv("dataset/tmdb_5000_credits.csv")

# ======================================
# Merge Datasets
# ======================================

movies = movies.merge(credits, on="title")

# ======================================
# Select Useful Columns
# ======================================

movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

# ======================================
# Dataset information
# ======================================

print(movies.head())

print("\nDataset Shape:")
print(movies.shape)