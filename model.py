import pandas as pd

#Load The Movie Dataset
movies = pd.read_csv("dataset/tmdb_5000_movies.csv")

#Display The First Five Rows
print(movies.head())