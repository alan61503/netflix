import pandas as pd
import numpy as np
from surprise import SVD
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy

# Load dataset (MovieLens-style CSV: userId, movieId, rating)
df = pd.read_csv("ratings.csv")  # Ensure CSV has 'userId', 'movieId', 'rating'

# Define Reader object for Surprise Library
reader = Reader(rating_scale=(0.5, 5.0))
data = Dataset.load_from_df(df[["userId", "movieId", "rating"]], reader)

# Split dataset into train and test sets
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Train an SVD model
model = SVD()
model.fit(trainset)

# Predict on test set
predictions = model.test(testset)

# Check accuracy
print(f"RMSE: {accuracy.rmse(predictions)}")

# Movie titles dataset
movies_df = pd.read_csv("movies.csv")  # Ensure CSV has 'movieId', 'title'

# Function to get movie recommendations for a user
def recommend_movies(user_id, num_recommendations=5):
    # Get list of all movie IDs
    movie_ids = df["movieId"].unique()

    # Predict ratings for all movies
    predicted_ratings = [model.predict(user_id, movie_id).est for movie_id in movie_ids]

    # Sort movies by predicted rating
    movie_ratings = list(zip(movie_ids, predicted_ratings))
    movie_ratings.sort(key=lambda x: x[1], reverse=True)

    # Get top N recommended movies
    top_movies = movie_ratings[:num_recommendations]

    # Convert movie IDs to titles
    recommended_titles = [movies_df[movies_df["movieId"] == movie_id]["title"].values[0] for movie_id, _ in top_movies]

    return recommended_titles

# Example usage
user_id = 1  # Change this to an existing user ID
recommended = recommend_movies(user_id)
print(f"Recommended movies for User {user_id}: {recommended}")
