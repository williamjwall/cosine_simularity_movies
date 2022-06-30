#from prueba import get_data


def output(movie_title):
    data = get_data()
    movie_data = data.loc[data['title'] == movie_title]
    text = movie_data['text']
    duration = movie_data['duration']
    genre = movie_data['genre']
    title = movie_data['title']
    return text, duration, genre, title
