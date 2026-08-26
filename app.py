from flask import Flask, render_template, request
import pickle

#create
app = Flask(__name__)

#load saved recommendation data
movies = pickle.load(open("movies.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))
print (movies.columns)
print(movies["title"].head(20))
#recommendation function
def recommend(movie_name):
    movie_name = movie_name.lower().strip()
    matches = movies[
        movies["title"].str.lower().str.strip() == movie_name 
    ]

    print("MATCHES")
    print(matches)
    if matches.empty:
     return[]

    movie_index = matches.index[0] 
    print("MOVIE INDEX:",movie_index)
    distance = similarity[movie_index]
    movie_list = sorted(
       list(enumerate(distance)),
       reverse = True,
       key=lambda x:x[1]
    )[1:6]
    print("MOVIE LIST:",movie_list)
    recommendations = []
    for i, score in movie_list:
       recommendations.append(movies.iloc[i] ["title"])
       print("RECOMMENDATIONS:",recommendations)
    return recommendations
#Home page
@app.route("/",methods=["GET","POST"])
def home():
    recommendations=[]
    movie_name = ""

    if request.method == "POST":
     movie_name = request.form["movie"]
     recommendations = recommend(movie_name)
    return render_template(
      "index.html",
       recommendations=recommendations,
       movie_name = movie_name
)
#Start
if __name__ == "__main__":
     app.run(debug=True)