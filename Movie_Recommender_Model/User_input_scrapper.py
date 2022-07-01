import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
# to get the search id for the movie for the URL
import imdb


class User_Input():
    def USERS_movie(movie):
        # creating instance of IMDb
        ia = imdb.IMDb()
        # searching the movie
        search = ia.search_movie(movie)
        return search[0].movieID

    def User_data(title):
        URL = "https://www.imdb.com/title/tt" + str(User_Input.USERS_movie(title))
        response = requests.get(URL, headers={"Accept-Language":"en-US"})
        soup = BeautifulSoup(response.content, "html.parser")
        img_data = soup.select('div img')[0]
        text = soup.find("span", class_="sc-16ede01-0 fMPjMP").string
        genre = []
        for i in soup.find_all("li", class_="ipc-inline-list__item ipc-chip__text"):
            genre.append(i.string)

        genre = ", ".join(genre)

        return [{'Text': text, 'Genre': genre, 'Image': img_data}]