import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy
from collections import defaultdict

def load_data(ratings_path):
    reader = Reader(line_format='user item rating', sep=',', skip_lines=1)
    data = Dataset.load_from_file(ratings_path, reader=reader)
    return data

def train_model(data):
    trainset, testset = train_test_split(data, test_size=0.2)
    model = SVD()
    model.fit(trainset)
    predictions = model.test(testset)
    print("RMSE:", accuracy.rmse(predictions))
    return model, trainset

def get_top_n_recommendations(model, trainset, user_id, n=5):
    all_movie_ids = set([trainset.to_raw_iid(i) for i in range(trainset.n_items)])
    rated_movies = {trainset.to_raw_iid(i) for (i, _) in trainset.ur[user_id]}
    unrated_movies = all_movie_ids - rated_movies
    
    predictions = [(movie, model.predict(user_id, movie).est) for movie in unrated_movies]
    top_n = sorted(predictions, key=lambda x: x[1], reverse=True)[:n]
    return top_n

if __name__ == "__main__":
    ratings_path = "ratings.csv"  # Ensure you have this file in the same directory
    data = load_data(ratings_path)
    model, trainset = train_model(data)
    
    user_id = 1  # Change this to test different users
    recommendations = get_top_n_recommendations(model, trainset, user_id, n=5)
    
    print("Recommended movies for user", user_id)
    for movie_id, score in recommendations:
        print(f"Movie ID: {movie_id}, Predicted Rating: {score:.2f}")