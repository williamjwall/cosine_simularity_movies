import pickle
import os
import pandas as pd

PATH = os.path.join(os.path.dirname(__file__), "data", "nico_movie_recommender.csv")

def get_data():
    return pd.read_csv(PATH, index_col = 'Unnamed: 0')

def get_pickle():
    pkl = os.path.join(os.path.dirname(__file__), "data", "title_embeddings.pkl")
    return pickle.load(open(pkl, 'rb'))
