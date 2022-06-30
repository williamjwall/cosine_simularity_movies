import requests
from bs4 import BeautifulSoup
# to get the search id for the movie for the URL
import imdb

class User_Input:

    def __init__(self):
        self

    def USERS_movie(self, movie):
        # creating instance of IMDb
        ia = imdb.IMDb()
        # searching the movie
        search = ia.search_movie(movie)
        return search[0].movieID

    def User_data(self):
        URL = "https://www.imdb.com/title/tt" + str(USERS_movie('Tarzan the wonder car'))
        response = requests.get(URL, headers={"Accept-Language":"en-US"})
        soup = BeautifulSoup(response.content, "html.parser")
        title = 'title' #this will be the users input
        text = soup.find("span", class_="sc-16ede01-0 fMPjMP").string
        genre = []
        for i in soup.find_all("li", class_="ipc-inline-list__item ipc-chip__text"):
            genre.append(i.string)

        genre = ", ".join(genre)

        return [{"Title": title, 'Text': text, 'Genre': genre}]
