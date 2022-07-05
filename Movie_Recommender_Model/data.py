import os
import pandas as pd


PATH = os.path.join(os.path.dirname(__file__), "data", "nico_movie_recommender.csv")
print(PATH)
def get_data():
    return pd.read_csv(PATH, index_col = 'Unnamed: 0')
