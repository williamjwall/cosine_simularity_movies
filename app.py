import streamlit as st

from Movie_Recommender_Model.data import *

from Movie_Recommender_Model.User_input_scrapper import User_Input
User_Input = User_Input()

from Movie_Recommender_Model.Model import MovieAssigner

# Our defult movie shown
dict = get_pickle()
MovieAssigner = MovieAssigner()
text = 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.'
df = MovieAssigner.get_3_most_similar_movies(text, dict)


st.markdown("""# Movie Recommender App
## Input the name of a movie you like, and the app will recomend you 3 other movies based on your input.""")

input_movie = st.text_input('Movie title', 'Ex: Inception')
if st.button('find movie'):
    st.write('The current movie title is', input_movie)
    movie = User_Input.USERS_movie(input_movie)
    user_df = User_Input.User_data(movie)
    df = MovieAssigner.get_3_most_similar_movies(user_df[0]['Text'], dict)



st.markdown("""## You can also write your own story! We'll output 3 movies based off the story you've written!""")
input_story = st.text_input('story', 'Ex: write your own story here')
if st.button('submit story'):
    st.write('The current story is', input_story)
    df = MovieAssigner.get_3_most_similar_movies(input_story, dict)


col1, col2, col3 = st.columns(3)

with col1:
    movie = User_Input.USERS_movie(df[0])
    st.header(df[0])
    tim = User_Input.User_data(movie)[0]
    st.image(str(tim.get('Image')).split('190w,')[1].split('285w')[0].strip())

with col2:
    movie = User_Input.USERS_movie(df[1])
    st.header(df[1])
    tim = User_Input.User_data(movie)[0]
    st.image(str(tim.get('Image')).split('190w,')[1].split('285w')[0].strip())

with col3:
    movie = User_Input.USERS_movie(df[2])
    st.header(df[2])
    tim = User_Input.User_data(movie)[0]
    st.image(str(tim.get('Image')).split('190w,')[1].split('285w')[0].strip())
