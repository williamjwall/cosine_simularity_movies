import pandas as pd
import requests
from bs4 import BeautifulSoup
import os


class Data:
    def importdata():
        URL = 'https://www.imdb.com/search/title/?countries=us&title_type=feature&num_votes=10000,&sort=user_rating,desc&'

        movies = []

        for i in range(1,144):
            if i == 1:
                response = requests.get(URL + 'ref_=adv_prv', headers={"Accept-Language":"en-US"})
                soup = BeautifulSoup(response.content, "html.parser")

            elif i > 1:
                response = requests.get(URL +'start='+str(((i-1)*50)+1)+'&ref_=adv_prv' , headers={"Accept-Language":"en-US"})
                soup = BeautifulSoup(response.content, "html.parser")



            for movie in soup.find_all("div", class_="lister-item-content"):
                title = movie.find("h3").find("a").string
                duration = int(movie.find("span", class_="runtime").string.strip(' min'))
                genre = movie.find("span", class_="genre").string.strip(' min').lstrip('\n')
                text = movie.find_all("p", class_="text-muted")[1].text.lstrip('\n')
                movies.append({'title': title, 'genre': genre, 'duration': duration, 'text': text})

        movies_df = pd.DataFrame(movies)
        return movies_df

    def get_data(self):
        half_path = os.path.dirname(os.path.dirname(__file__))
        full_path = os.path.join(half_path, "raw_data", "nico_movie_recommender.csv" )
        df = pd.read_csv(full_path)
        return df
