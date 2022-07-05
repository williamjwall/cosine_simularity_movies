import streamlit as st
from Movie_Recommender_Model import User_input_scrapper

from Movie_Recommender_Model.User_input_scrapper import User_Input
from Movie_Recommender_Model.Module import MovieAssigner

st.markdown("""# Movie Recommender App
## Input the name of a movie you like, and the app will recomend you 3 other movies based on your input.
We use natural language processing to recommend you the movies""")

text = st.text_input('Movie title', 'Ex: Life of Brian')
st.write('The current movie title is', text)

st.markdown("""## You can also write your own story! We'll output 3 movies based off the story you've written!""")
text = st.text_input('story')


def User(text):
    return User_Input.User_data(text)

col1, col2, col3 = st.columns(3)

df = MovieAssigner.calling_func(User)

with col1:
    st.header(df[0])

with col2:
    st.header(df[1])

with col3:
    st.header(df[2])
