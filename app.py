
import streamlit as st

import numpy as np
import pandas as pd

#from Movie_Recommender_Model.webscrapping import get_data
from Movie_Recommender_Model.webscrapping import get_data

# def output(movie_title):
#     data = get_data()
#     movie_data = data.loc[data['title'] == movie_title]
#     text = movie_data['text']
#     duration = movie_data['duration']
#     genre = movie_data['genre']
#     title = movie_data['title']
#     return text, duration, genre, title

st.markdown("""# Movie Recommender App
## Input the name of a movie you like, and the app will recomend you 3 other movies based on your input.
We use natural language processing to recommend you the movies""")


title = st.text_input('Movie title', 'Ex: Life of Brian')
st.write('The current movie title is', title)




col1, col2, col3 = st.columns(3)

with col1:
    st.header(get_data('The Godfather')[3])


with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
