import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("data/movies.csv")

# Select useful columns
movies = movies[['title', 'overview']]

# Handle missing values
movies['overview'] = movies['overview'].fillna('')

# Convert text to numerical vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend_movies(movie_title, num_recommendations=5):
    if movie_title not in movies['title'].values:
        print("Movie not found!")
        return

    idx = movies[movies['title'] == movie_title].index[0]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    top_movies = similarity_scores[1:num_recommendations+1]
    for i in top_movies:
        print(movies.iloc[i[0]]['title'])

# Test
recommend_movies("Avatar")
