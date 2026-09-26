# 🎬 Movie Recommendation System

An AI-based movie recommendation web application that recommends movies similar to a user's selected movie.

## 📌 Project Overview

This project uses **content-based filtering** to recommend movies based on movie information such as overview, genres, keywords, cast, and director.

The project uses the **TMDB 5000 Movie Dataset** and calculates movie similarity using **CountVectorizer** and **Cosine Similarity**.

The recommendation system is deployed as a **Flask web application** with a professional red and white user interface.

## 🚀 Features

- 🎬 Content-based movie recommendations
- 🔍 Movie search
- 🤖 Machine learning-based similarity calculation
- 🎨 Red and white professional UI
- ✨ Floating movie recommendation cards
- 🌐 Flask web application
- 📊 Movie metadata-based recommendations

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS
- TMDB 5000 Movie Dataset

## 🧠 How It Works

1. Load the TMDB movies and credits datasets.
2. Merge the datasets using the movie ID.
3. Select useful movie information.
4. Extract genres, keywords, cast, and director information.
5. Combine the information into a `tags` column.
6. Convert the tags into numerical vectors using `CountVectorizer`.
7. Calculate similarity using `Cosine Similarity`.
8. Find movies similar to the selected movie.
9. Display the recommendations through the Flask web application.

## 📂 Project Structure

```text
Movie_Recommendation_System/
├── dataset/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── model.py
├── movies.pkl
├── similarity.pkl
├── README.md
├── requirements.txt
└── .gitignore
```

> `similarity.pkl` is kept locally and excluded from GitHub because of its large file size.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Move into the Project Directory

```bash
cd Movie_Recommendation_System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Flask Application

```bash
python app.py
```

### 7. Open the Application

```text
http://127.0.0.1:5000
```

### 8. Enter a Movie

Example:

```text
Avatar
```

or

```text
Titanic
```

The system will display movies similar to the selected movie.

## 🧮 Recommendation Method

This project uses **content-based filtering**.

Movie information is combined into a `tags` representation.

`CountVectorizer` converts the text information into numerical vectors.

`Cosine Similarity` is then used to measure the similarity between movies.

Movies with the highest similarity scores are selected as recommendations.

## 📊 Dataset

The project uses the **TMDB 5000 Movie Dataset**.

The dataset contains:

- Movie titles
- Movie overviews
- Genres
- Keywords
- Cast
- Crew

## 🎯 Future Improvements

- 🎞️ Movie posters
- ⭐ Movie ratings
- 👤 Personalized recommendations
- 🔎 Search autocomplete
- 🧠 Advanced NLP techniques
- ☁️ Cloud deployment
- 📱 Improved mobile responsiveness
- 🎭 Genre-based filtering

## 🎓 Project Purpose

This project demonstrates:

- Machine Learning
- Data preprocessing
- Feature extraction
- Content-based recommendation
- Cosine Similarity
- Python
- Flask web development
- Git and GitHub

## 👨‍💻 Project

**Movie Recommendation System**

Built using **Python, Machine Learning, and Flask**.