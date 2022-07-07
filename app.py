import streamlit as st
import requests

st.markdown("""# Movie Recommender App
## Input the name of a movie you like, and the app will recomend you 3 other movies based on your input.""")

input_movie = st.text_input('Movie title', 'Ex: Inception')
if st.button('find movie'):
    st.write('The current movie title is', input_movie)

st.markdown("""## You can also write your own story! We'll output 3 movies based off the story you've written!""")
input_story = st.text_input('story', 'Ex: write your own story here')
if st.button('submit story'):
    st.write('The current story is', input_story)

url = 'http://127.0.0.1:8000/predict/'
url1 = 'http://127.0.0.1:8000/predictstory/'

params = {'input_movie': input_movie}
params1 = {'input_story': input_story}

response = requests.get(url, params=params)
response1= requests.get(url1, params=params1)

movie_response = response.json()
story_response = response1.json()

col1, col2, col3 = st.columns(3)
st.write(movie_response)
with col1:
    st.header(movie_response['movies'][0])
    st.image(movie_response['links'][0])

with col2:
    st.header(movie_response['movies'][1])
    st.image(movie_response['links'][1])

with col3:
    st.header(movie_response['movies'][2])
    st.image(movie_response['links'][2])
