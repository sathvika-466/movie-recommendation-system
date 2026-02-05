# Movie Recommendation System

This project is a **content-based movie recommendation system** built using Python and Machine Learning.  
It recommends movies similar to a given movie based on their plot descriptions.

## Features
- Recommends movies based on content similarity
- Uses Natural Language Processing (NLP)
- Beginner-friendly implementation

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Cosine Similarity

## 📂 Project Structure
movie-recommendation-system
│
├── data
│ └── movies.csv
│
├── src
│ └── movie_recommender.py
│
├── README.md
└── requirements.txt


---

## ⚙️ How It Works
1. Loads movie data from a CSV file
2. Cleans and preprocesses text data
3. Converts text into TF-IDF vectors
4. Computes cosine similarity between movies
5. Recommends similar movies

##  How to Run the Project

1. Install dependencies:
```bash
pip install -r requirements.txt

2. Run the program:
```bash 
python src/movie_recommender.py
