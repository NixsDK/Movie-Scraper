import sqlite3
import os

def setup_database():
    db_folder = "database"
    db_path = os.path.join(db_folder, "movies.db")

    # Ensure the database folder exists
    os.makedirs(db_folder, exist_ok=True)

    # Connect to the database, which creates it if it doesn't exist
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the movies table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT,
            release_year INTEGER,
            rating REAL
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Database setup completed. Database path: {db_path}")

if __name__ == "__main__":
    setup_database()
