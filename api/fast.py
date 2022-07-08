from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Movie_Recommender_Model.Model import MovieAssigner
from Movie_Recommender_Model.User_input_scrapper import User_Input
from Movie_Recommender_Model.data import get_pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return "here"

@app.get("/predict")
def predict(input_movie):
    dict = get_pickle()
    movie = User_Input().USERS_movie(input_movie)
    user_df = User_Input().User_data(movie)
    movies = MovieAssigner().get_3_most_similar_movies(user_df[0]['Text'], dict)
    link1 = User_Input().User_data(User_Input().USERS_movie(movies[0]))[0]["Image"]["srcset"].split('190w,')[1].split('285w')[0].strip()
    link2 = User_Input().User_data(User_Input().USERS_movie(movies[1]))[0]["Image"]["srcset"].split('190w,')[1].split('285w')[0].strip()
    link3 = User_Input().User_data(User_Input().USERS_movie(movies[2]))[0]["Image"]["srcset"].split('190w,')[1].split('285w')[0].strip()
    return {'movies': movies, 'links':[link1, link2, link3]}

@app.get("/predictstory")
def predictstory(input_story):
    dict = get_pickle()
    movies = MovieAssigner().get_3_most_similar_movies(input_story, dict)
    link1 = User_Input().User_data(User_Input().USERS_movie(movies[0]))[0]["Image"]["srcset"].split('190w,')[1].split('285w')[0].strip()
    link2 = User_Input().User_data(User_Input().USERS_movie(movies[1]))[0]["Image"]["srcset"].split('190w,')[1].split('285w')[0].strip()
    link3 = User_Input().User_data(User_Input().USERS_movie(movies[2]))[0]["Image"]["srcset"].split('190w,')[1].split('285w')[0].strip()
    return {'movies': movies, 'links':[link1, link2, link3]}
