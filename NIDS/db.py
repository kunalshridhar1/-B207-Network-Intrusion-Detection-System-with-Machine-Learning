import sqlite3

# Connect to SQLite DB
conn = sqlite3.connect("phishing.db")
cursor = conn.cursor()

# Create table if not exists (initial structure)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email_text TEXT,
        prediction TEXT,
        timestamp TEXT
    )
''')

# Check if 'features' column exists
cursor.execute("PRAGMA table_info(predictions)")
columns = [column[1] for column in cursor.fetchall()]
if "features" not in columns:
    cursor.execute("ALTER TABLE predictions ADD COLUMN features TEXT")
    print("[+] 'features' column added to existing 'predictions' table.")
else:
    print("[=] 'features' column already exists.")

conn.commit()
conn.close()
print("[✓] Database is ready.")
# This script initializes the SQLite database for the phishing email detection application.
# It creates the 'predictions' table if it doesn't exist and checks for the 'features' column.  
# If the 'features' column is missing, it adds it to the existing table.
# The database is used to store email predictions and their features for later analysis.    
# This script is designed to set up the database for the phishing email detection application.
# Make sure to run this script before running the main prediction script to ensure the database is ready
