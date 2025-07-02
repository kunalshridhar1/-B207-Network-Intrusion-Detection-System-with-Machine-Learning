import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
import joblib
from preprocess import clean_email  # Make sure preprocess.py has this function

def train_model():
    # Load the updated CSV with full email fields
    df = pd.read_csv("train.csv")

    # Combine and clean the fields into one input string
    df['combined'] = df.apply(lambda row: clean_email(row['from'], row['to'], row['subject'], row['body']), axis=1)

    # Vectorize the text data
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['combined'])
    y = df['label']

    # Split data and train the model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Print performance report
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Save model and vectorizer
    joblib.dump(model, "phishing_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

if __name__ == "__main__":
    train_model()
# This script trains a model to classify emails as phishing or ham using the provided CSV file.
# It uses a Random Forest classifier and TF-IDF vectorization for text data.        
# The trained model and vectorizer are saved as 'phishing_model.pkl' and 'vectorizer.pkl'.
# Make sure to have the 'train.csv' file in the same directory as this script.   