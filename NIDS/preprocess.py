import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_email(from_addr, to_addr, subject, body):
    full_text = f"{from_addr} {to_addr} {subject} {body}".lower()
    full_text = re.sub(r"http\S+|www\S+|https\S+", '', full_text)
    full_text = re.sub(r'\b\d+\b', '', full_text)
    full_text = full_text.translate(str.maketrans('', '', string.punctuation))
    return full_text
