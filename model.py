import pandas as pd

# Load The Movie Dataset
movies = pd.read_csv("dataset/tmdb_5000_movies.csv")
credits = pd.read_csv("dataset/tmdb_5000_credits.csv")

# ======================================
# Dataset information
# ======================================

print("Movies Dataset Shape:")
print(movies.shape)

print("\nCredits Dataset Shape:")
print(credits.shape)

print("\nMovies Columns")
print(movies.columns)

print("\nCredits Columns")
print(credits.columns)