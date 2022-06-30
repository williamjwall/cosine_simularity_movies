import data
import string
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from User_input_scrapper import User_Input

class Clean_To_Vectorize:

    def __init__(self):
        self.movies_df = data.get_data()
        self.movies_df.drop('Unnamed: 0', inplace=True, axis=1)
        self.Users_movie = User_Input.User_data()

    def cleaning(self, series):
        sentence = series.strip()
        sentence = sentence.lower()
        sentence = ''.join(char for char in sentence if not char.isdigit())
        for punctuation in string.punctuation:
            sentence = sentence.replace(punctuation, '')

        sentence = word_tokenize(sentence)

        tokens_cleaned = [word for word in sentence if not word in stop_words]

        lemmatized_sentence = []
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()

        for i in tokens_cleaned:
                lemmatized = lemmatizer.lemmatize(i)
                lemmatized_sentence.append(lemmatized)
        return lemmatized_sentence

    def vectorizer(self, series):
        tf_idf_vectorizer = TfidfVectorizer()
        vector_txts = tf_idf_vectorizer.fit_transform(series)
        return vector_txts.toarray()

    def Movies_Clean_Vectorized(self):
        self.movies_df[['cleaned_texts']] = self.movies_df[['text']].applymap(self.cleaning)
        self.movies_df['vectorized_texts'] = self.movies_df['cleaned_texts'].apply(self.vectorizer)

    def Users_Clean_Vectorized(self):
        self.Users_movie[['cleaned_texts']] = self.Users_movie[['text']].applymap(self.cleaning)
        self.Users_movie['vectorized_texts'] = self.Users_movie['cleaned_texts'].apply(self.vectorizer)
