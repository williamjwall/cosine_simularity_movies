import streamlit as st

import numpy as np
import pandas as pd


from Movie_Recommender_Model.webscrapping import get_data

from Movie_Recommender_Model.User_input_scrapper import User_Input







st.markdown("""# Movie Recommender App
## Input the name of a movie you like, and the app will recomend you 3 other movies based on your input.
We use natural language processing to recommend you the movies""")


title = st.text_input('Movie title', 'Ex: Life of Brian')
st.write('The current movie title is', title)

User_Input.User_data(title)

st.button('Run Model', key=None, help=None, on_click=None, args=None, kwargs=None, disabled=False)





col1, col2, col3 = st.columns(3)

with col1:
    string = get_data('Iron Man')[3]
    newstring = ''.join([i for i in string if not i.isdigit()])
    st.header(newstring)
    tim = User_Input.User_data('Iron Man')[0]
    st.image(str(tim.get('Image')).split('190w,')[1].split('285w')[0].strip())

with col2:
    string = get_data('The Godfather')[3]
    newstring = ''.join([i for i in string if not i.isdigit()])
    st.header(newstring)
    tim = User_Input.User_data('The Godfather')[0]
    st.image(str(tim.get('Image')).split('190w,')[1].split('285w')[0].strip())

with col3:
    string = get_data('Hulk')[3]
    newstring = ''.join([i for i in string if not i.isdigit()])
    st.header(newstring)
    tim = User_Input.User_data('Hulk')[0]
    st.image(str(tim.get('Image')).split('190w,')[1].split('285w')[0].strip())
