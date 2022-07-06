import pickle
import os
import pandas as pd


PATH = os.path.join(os.path.dirname(__file__), "data", "nico_movie_recommender.csv")

def get_data():
    return pd.read_csv(PATH, index_col = 'Unnamed: 0')

def get_movie(movie_title):
    data = pd.read_csv(PATH, index_col = 'Unnamed: 0')
    movie_data = data.loc[data['title'] == movie_title]
    text = movie_data['text']
    duration = movie_data['duration']
    genre = movie_data['genre']
    title = movie_data['title']
    return text, duration, genre, title

def get_pickle():
    pkl = os.path.join(os.path.dirname(__file__), "data", "title_embeddings.pkl")
    return pickle.load(open(pkl, 'rb'))
