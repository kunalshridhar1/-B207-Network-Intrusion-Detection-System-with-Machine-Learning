# 📧 Phishing Email Detection System using Machine Learning

This project is a simple yet effective **Network Intrusion Detection System (NIDS)** that detects **phishing emails** using **machine learning**. It analyzes the content of an email (sender, receiver, subject, and body) and predicts whether the message is **phishing** or **ham (safe)**.

---

## ✅ Features

### 📌 Core Features (Required)
- [x] Preprocess and clean email content
- [x] Extract features using **TF-IDF Vectorizer**
- [x] Train a **Random Forest Classifier** using `scikit-learn`
- [x] Predict phishing attempts from command line
- [x] Display results with basic reporting
- [x] Store predictions in an SQLite database

### 🌟 Extended Features (Bonus)
- [x] Store **TF-IDF vectors** (features) in the database for future reference
- [x] `features` column is Base64 + Pickle encoded for compact storage
- [x] Schema migration handled via `db.py`

---

## 🛠 Technologies Used
- **Python**
- **scikit-learn**
- **pandas**
- **SQLite3**
- **argparse**
- **joblib**, **pickle**, **base64**

---

## 🚀 How to Run

 1. 🔧 Train the model

bash
python  model.py
-Trains the classifier and saves:

    "phishing_model.pkl"

    "vectorizer.pkl"


2. 🧱 Initialize or upgrade the database
 
bash

python db.py
Creates phishing.db and ensures the table + features column exists.


3. 📬 Test an email for phishing detection
bash

python main.py --from_ "hr@company.com" --to "user@example.com" --subject "Urgent Update" --body "Please verify your account by clicking the link."
✅ Output:

pgsql

[+] Prediction: PHISHING
[+] Result saved to database.
[+] You can view the results in the database using a database viewer or query tool.

🗂 Example train.csv Format
text	                                                            label
"Your account has been suspended. Click here to reactivate it."	    phishing
"Reminder: Project deadline extended to next Friday."	            ham

🧠 Output Schema (phishing.db)
Column	     Type	  Description
id	         INTEGER  Auto-increment ID
email_text	 TEXT	  Full email text
prediction	 TEXT	  phishing or ham
timestamp	 TEXT	  Prediction timestamp
features	 TEXT	  Base64-encoded TF-IDF feature vector

📂 Project Structure
📁 NIDS/
├── model.py          # Trains the ML model
├── main.py           # CLI phishing detection
├── db.py             # DB schema initialization
├── phishing.db       # SQLite database
├── train.csv         # Training data
├── phishing_model.pkl
├── vectorizer.pkl
└── README.md         # This file

🧪 Evaluation Metrics
Precision, Recall, F1-score displayed after training

Example:

              precision    recall  f1-score   support
      ham         0.95       0.97      0.96       400
  phishing        0.96       0.93      0.94       300

📌 Author
Kunal Shridhar
Github:kunalshridhar1
