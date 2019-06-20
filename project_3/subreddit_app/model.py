from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from utilities import clean_text
import pandas as pd

class LemmaTokenizer(object):

    def __init__(self):
        self.wnl = WordNetLemmatizer()

    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]

# function to parse text and spit out prediction based on 2 classes:


def classify_text(text, mdl):

    parsed_text = [clean_text(text)]
    return mdl.predict_proba(parsed_text)



