import argparse
import sqlite3
import joblib
import re
import string
import pickle
import base64
from datetime import datetime

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def combine_email(from_, to, subject, body):
    return f"{from_} {to} {subject} {body}"

# Load model and vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Database connection
conn = sqlite3.connect("phishing.db")
cursor = conn.cursor()

# Ensure table exists with 'features' column
cursor.execute('''
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email_text TEXT,
        prediction TEXT,
        timestamp TEXT,
        features TEXT
    )
''')

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Phishing Email Detector")
parser.add_argument("--from_", required=True, help="Email sender")
parser.add_argument("--to", required=True, help="Email recipient")
parser.add_argument("--subject", required=True, help="Email subject")
parser.add_argument("--body", required=True, help="Email body")
args = parser.parse_args()

# Prepare input
email_text = combine_email(args.from_, args.to, args.subject, args.body)
cleaned_text = clean_text(email_text)
features = vectorizer.transform([cleaned_text])
prediction = model.predict(features)[0]

# Serialize TF-IDF features
serialized_features = base64.b64encode(pickle.dumps(features)).decode("utf-8")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Store in DB
cursor.execute('''
    INSERT INTO predictions (email_text, prediction, timestamp, features)
    VALUES (?, ?, ?, ?)
''', (email_text, prediction, timestamp, serialized_features))

conn.commit()
conn.close()

# Output
print(f"[+] Prediction: {prediction.upper()}")
print("[+] Result saved to database.")
print("[+] You can view the results in the database using a database viewer or query tool.")

# This script is designed to predict whether an email is phishing or not.
# It uses a trained model and vectorizer to process the email fields and make predictions.      
# This script can be run from the command line to predict phishing emails.
# It initializes a database to save the results and provides a user-friendly output.
# Make sure to have the necessary files (phishing_model.pkl, vectorizer.pkl, and preprocess.py) in the same directory as this script.
# The database is initialized and results are saved in 'phishing.db'.