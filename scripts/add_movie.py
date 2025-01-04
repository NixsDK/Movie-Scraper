import sqlite3
import os

DB_PATH = "database/movies.db"
MOVIES_FILE = "scripts/movies.txt"

def add_movie(title, genre, release_year, rating):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO movies (title, genre, release_year, rating)
        VALUES (?, ?, ?, ?)
    ''', (title, genre, release_year, rating))

    conn.commit()
    conn.close()
    print(f"Movie '{title}' added to the database.")

def add_movies_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Skip empty lines or lines starting with a comment
            if not line.strip() or line.startswith("#"):
                continue

            # Parse the line
            try:
                title, genre, release_year, rating = line.strip().split('|')
                add_movie(title, genre, int(release_year), float(rating))
            except ValueError as e:
                print(f"Skipping line due to parsing error: {line.strip()} ({e})")

if __name__ == "__main__":
    print("1. Add a single movie")
    print("2. Add movies from file")

    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        # Add a single movie
        title = input("Enter movie title: ")
        genre = input("Enter movie genre: ")
        release_year = int(input("Enter release year: "))
        rating = float(input("Enter movie rating: "))
        add_movie(title, genre, release_year, rating)

    elif choice == "2":
        # Add movies from file
        add_movies_from_file(MOVIES_FILE)

    else:
        print("Invalid choice. Exiting.")
