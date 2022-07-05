import requests
from bs4 import BeautifulSoup
# to get the search id for the movie for the URL
import imdb

class User_Input:

    def USERS_movie(movie):
        ia = imdb.IMDb()
        # searching the movie to get the encoded title
        search = ia.search_movie(movie)
        return search[0].movieID

    def User_data(streamlit_title):
        URL = "https://www.imdb.com/title/tt" + str(User_Input.USERS_movie(streamlit_title)) #users input from stream lit
        response = requests.get(URL, headers={"Accept-Language":"en-US"})
        soup = BeautifulSoup(response.content, "html.parser")
        title = 'title' #this will be the users input
        text = soup.find("span", class_="sc-16ede01-0 fMPjMP").string
        genre = []
        for i in soup.find_all("li", class_="ipc-inline-list__item ipc-chip__text"):
            genre.append(i.string)

        genre = ", ".join(genre)

        return [{"Title": title, 'Text': text, 'Genre': genre}]
