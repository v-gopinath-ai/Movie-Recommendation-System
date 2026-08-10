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
# Clean The Dataset
# ======================================

print ("Missing values before cleaning:")
print(movies.isnull().sum())

# Remove movies without an overview
movies.dropna(subset=["overview"],inplace=True)

# Fill Other missing values
movies["genres"] = movies["genres"].fillna("[]")
movies["keywords"] = movies["keywords"].fillna("[]")
movies["cast"] = movies["cast"].fillna("[]")
movies["crew"] = movies["crew"].fillna("[]")

# Reset index
movies.reset_index(drop=True,inplace=True)

# Check the cleaned dataset
print("\nMissing values after cleaning:")
print(movies.isnull().sum())

print("\nCleaned dataset shape:")
print(movies.shape)

# ======================================
# Dataset information
# ======================================

print(movies.head())

print("\nDataset Shape:")
print(movies.shape)