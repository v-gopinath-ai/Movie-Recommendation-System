import pandas as pd

# Load The Movie Dataset
movies = pd.read_csv("dataset/tmdb_5000_movies.csv")
credits = pd.read_csv("dataset/tmdb_5000_credits.csv")

# ======================================
# Merge Datasets
# ======================================

movies = movies.merge(credits, on="title")

# ======================================
# Dataset information
# ======================================

print("Merged Dataset Shape")
print(movies.shape)

print("\n")

print("First 5 Rows:")
print(movies.head())