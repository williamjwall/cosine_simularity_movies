import pandas as pd
import numpy as np
import data
from sentence_transformers import SentenceTransformer, util

class MovieAssigner():
    def __init__(self):
        self.df = data.get_data()

    # Here we embed the descriptions of the movies --> shape (7150, 384)
    # No matter the len of the texts it will be embeded as 384
    def embed_sentences(self):
        sentences = np.array(self.df['text'])

        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        embedded_sentences = model.encode(sentences, convert_to_numpy = True)
        return embedded_sentences

    # Here we create a list of titles so that we can zip it with the sentences maintaing the movies ID with the description
    def get_embbedings_dict(self, embedded_sentences):

        titles = self.df['title'].to_list()

        title_embedding_dict = {}

        for key, value in zip(titles, embedded_sentences):
            title_embedding_dict[key] = value
        return title_embedding_dict

    # Here we input the new movies text, df, and our embedded sentences. We embed the new movies text. Fine cosine simularity
    # between new_move/new_text embedded to a list of our df embedded texts
    def get_3_most_similar_movies(self, new_movie_text, title_embedded_dict):

        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        new_movie_text_embedded = model.encode(new_movie_text, convert_to_numpy=True)

        arg_cos_sim = np.argsort(util.pytorch_cos_sim(new_movie_text_embedded, list(title_embedded_dict.values())))

        # This is to aviod outputing the Users movie of choice
        A = list(title_embedded_dict.values())[arg_cos_sim[0][-1]].round(4)
        B = new_movie_text_embedded.round(4)

        if np.array_equal(A, B) == True:
            first_arg_most_similar = arg_cos_sim[0][-2]
            second_arg_most_similar = arg_cos_sim[0][-3]
            third_arg_most_similar = arg_cos_sim[0][-4]
        else:
            first_arg_most_similar = arg_cos_sim[0][-1]
            second_arg_most_similar = arg_cos_sim[0][-2]
            third_arg_most_similar = arg_cos_sim[0][-3]

        #A list of keys indexed with the arg_cos_sim tensor position
        first_movie_most_sim = list(title_embedded_dict.keys())[first_arg_most_similar]
        second_movie_most_sim = list(title_embedded_dict.keys())[second_arg_most_similar]
        third_movie_most_sim = list(title_embedded_dict.keys())[third_arg_most_similar]

        return first_movie_most_sim, second_movie_most_sim, third_movie_most_sim

    def calling_func(self, User_Input):
        embedded_sentences = self.embed_sentences(self.df)
        return self.get_3_most_similar_movies(User_Input, self.df, embedded_sentences)

if __name__ == "__main__":
    df = data.get_data()
    MovieAssigner = MovieAssigner()
    sentences = MovieAssigner.embed_sentences(df)
    embedded_sentences = MovieAssigner.get_embbedings_dict(sentences)
    new_movie_text = "In 1936, archaeologist and adventurer Indiana Jones is hired by the U.S. government to find the Ark of the Covenant before Adolf Hitler's Nazis can obtain its awesome powers."
    three_movies = MovieAssigner.get_3_most_similar_movies(new_movie_text, embedded_sentences)
    print(three_movies)
