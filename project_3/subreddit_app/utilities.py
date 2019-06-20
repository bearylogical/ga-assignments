import regex as re
from nltk.corpus import stopwords


stops = set(stopwords.words('english'))


def clean_text(text):
    # 01 convert titles, selftext into lowercase
    lower_text = text.lower()
    no_br_paret_text = re.sub(r'\(.+?\)|\[.+?\]', ' ', str(lower_text))
    # 03 remove special characters
    removed_special = re.sub(r'[^0-9a-zA-Z ]+', ' ', str(no_br_paret_text))
    # 04 remove xamp200b
    remove_xamp200b = re.sub(r'ampx200b', ' ', str(removed_special))
    # 05 remove digits
    result = re.sub(r'\d+', '', remove_xamp200b).split()
    # 06 split into individual words
    meaningful_words = [w for w in result if not w in stops]

    # 07 Join the words back into one string separated by space,
    # and return the result.
    return " ".join(meaningful_words)

