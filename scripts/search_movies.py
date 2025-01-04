import sqlite3
import os

DB_PATH = "database/movies.db"
MOVIES_FILE = "scripts/top_250_movies.txt"

def load_movies_from_file():
    movies = []
    if not os.path.exists(MOVIES_FILE):
        print(f"File not found: {MOVIES_FILE}")
        return movies

    with open(MOVIES_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            # Skip empty lines or comments
            if not line.strip() or line.startswith("#"):
                continue
            try:
                title, genre, release_year, rating = line.strip().split('|')
                movies.append({
                    "title": title,
                    "genre": genre,
                    "release_year": int(release_year),
                    "rating": float(rating)
                })
            except ValueError as e:
                print(f"Skipping line due to parsing error: {line.strip()} ({e})")
    return movies

def search_movies_from_file(movies, query, search_by):
    results = []
    query = query.lower()
    for movie in movies:
        if search_by == "title" and query in movie["title"].lower():
            results.append(movie)
        elif search_by == "genre" and query in movie["genre"].lower():
            results.append(movie)
        elif search_by == "rating" and movie["rating"] >= float(query):
            results.append(movie)
    return results

def search_movies_by_title(title):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM movies WHERE title LIKE ?', (f"%{title}%",))
    results = cursor.fetchall()

    conn.close()
    return results

def search_movies_by_genre(genre):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM movies WHERE genre LIKE ?', (f"%{genre}%",))
    results = cursor.fetchall()

    conn.close()
    return results

def search_movies_by_rating(min_rating):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM movies WHERE rating >= ?', (min_rating,))
    results = cursor.fetchall()

    conn.close()
    return results

if __name__ == "__main__":
    movies_from_file = load_movies_from_file()

    print("Search Options:")
    print("1. Search by Title")
    print("2. Search by Genre")
    print("3. Search by Minimum Rating")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        query = input("Enter title to search: ")
        db_results = search_movies_by_title(query)
        file_results = search_movies_from_file(movies_from_file, query, "title")
    elif choice == "2":
        query = input("Enter genre to search: ")
        db_results = search_movies_by_genre(query)
        file_results = search_movies_from_file(movies_from_file, query, "genre")
    elif choice == "3":
        query = input("Enter minimum rating to search: ")
        db_results = search_movies_by_rating(float(query))
        file_results = search_movies_from_file(movies_from_file, query, "rating")
    else:
        print("Invalid choice!")
        db_results = []
        file_results = []

    print("\nSearch Results (From Database):")
    for row in db_results:
        print(row)

    print("\nSearch Results (From File):")
    for movie in file_results:
        print(f"{movie['title']} ({movie['release_year']}) - {movie['genre']} - {movie['rating']}")
