import requests
from bs4 import BeautifulSoup
# to get the search id for the movie for the URL
import imdb

class User_Input():
    def __init__(self):
        pass
    def USERS_movie(self, movie):
        self.movie = movie
        ia = imdb.IMDb()
        # searching the movie to get the encoded title
        search = ia.search_movie(self.movie)
        return search[0].movieID

    def User_data(self, str_title):
        self.str_title = str_title
        URL = "https://www.imdb.com/title/tt" + str(self.str_title) #users input from stream lit
        response = requests.get(URL, headers={"Accept-Language":"en-US"})
        soup = BeautifulSoup(response.content, "html.parser")
        img_data = soup.select('div img')[0]
        text = soup.find("span", class_="sc-16ede01-0 fMPjMP").text
        # genre = []
        # for i in soup.find_all("li", class_="ipc-inline-list__item ipc-chip__text"):
        #     genre.append(i.string)

        # genre = ", ".join(genre)

        return [{'Text': text, 'Image': img_data}]

if __name__ == "__main__":
    User_Input = User_Input()
    input_movie = "Inception"
    movie = User_Input.USERS_movie(input_movie)
    user_df = User_Input.User_data(movie)
