import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer

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
# Extract Movie information
# ======================================

def convert(text):
    items = ast.literal_eval(text)
    return [item["name"]for item in items]

def get_cast(text):
    items = ast.literal_eval(text)
    return[items["name"] for item in items[:3]]

def get_director(text):
    items = ast.literal_eval(text)

    for item in items:
        if item["job"] == "Director":
            return[item["name"]]
    return[]
    movies["genres"] = movies["genres"].apply(convert)
    movies["keywords"] = movies["keywords"].apply(convert)
    movies["cast"] = movies["cast"].apply(get_cast)
    movies["crew"] = movies["crew"].apply(get_director)

print("\nProcessed Movie information:")
print(movies[["title","genres","keywords","cast","crew"]].head())

# ======================================
# Create Tags
# ======================================

# Convert overview into a list of words
movies["overview"] = movies["overview"].apply(lambda x: x.split() if isinstance(x,str)else[])
for column in ["genres","keywords","cast","crew"]:
    movies[column] = movies[column].apply(lambda x: x if isinstance(x,list) else[] ) 
# Combine all important features
movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"]
                  )

# Convert the list into a single string
movies["tags"] = movies["tags"].apply(lambda x:"".join(map(str,x)))

# Keep only the columns we need
movies = movies[["movie_id","title","tags"]]

# ======================================
# Text Vectorization
# ======================================

cv = CountVectorizer(
    max_features = 5000,
    stop_words = "english"
)

vectors = cv.fit_transform(movies["tags"]).toarray()

print("\nVectorized Data Shape:")
print(vectors.shape)

# ======================================
# Dataset information
# ======================================
print("\nMovie Tags:")
print(movies.head())

print("\nDataset Shape:")
print(movies.shape)