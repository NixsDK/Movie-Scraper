import sqlite3
import os

# Path to the SQLite database
DB_PATH = "database/movies.db"

# Path to the text file containing top 250 movies
MOVIES_FILE = "scripts/top_250_movies.txt"

def load_movies_from_file():
    """
    Load movie data from the specified text file.
    Returns a list of movie dictionaries.
    """
    movies = []
    # Check if the file exists
    if not os.path.exists(MOVIES_FILE):
        print(f"File not found: {MOVIES_FILE}")
        return movies

    with open(MOVIES_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            # Skip empty lines or lines starting with a comment
            if not line.strip() or line.startswith("#"):
                continue
            try:
                # Parse the line into movie attributes
                title, genre, release_year, rating = line.strip().split('|')
                movies.append({
                    "title": title,
                    "genre": genre,
                    "release_year": int(release_year),  # Convert year to integer
                    "rating": float(rating)  # Convert rating to float
                })
            except ValueError as e:
                # Handle parsing errors and continue
                print(f"Skipping line due to parsing error: {line.strip()} ({e})")
    return movies

def search_movies_from_file(movies, query, search_by):
    """
    Search for movies in the provided list based on the query and search criteria.
    Args:
        movies: List of movie dictionaries to search.
        query: Search term.
        search_by: Criterion to search by ('title', 'genre', or 'rating').
    Returns:
        List of matching movies.
    """
    results = []
    query = query.lower()  # Normalize query for case-insensitive search
    for movie in movies:
        if search_by == "title" and query in movie["title"].lower():
            results.append(movie)
        elif search_by == "genre" and query in movie["genre"].lower():
            results.append(movie)
        elif search_by == "rating" and movie["rating"] >= float(query):
            results.append(movie)
    return results

def search_movies_by_title(title):
    """
    Search for movies in the database by title.
    Args:
        title: Title or part of the title to search for.
    Returns:
        List of matching rows from the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Use SQL query with a wildcard to search for titles
    cursor.execute('SELECT * FROM movies WHERE title LIKE ?', (f"%{title}%",))
    results = cursor.fetchall()

    conn.close()
    return results

def search_movies_by_genre(genre):
    """
    Search for movies in the database by genre.
    Args:
        genre: Genre to search for.
    Returns:
        List of matching rows from the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Use SQL query with a wildcard to search for genres
    cursor.execute('SELECT * FROM movies WHERE genre LIKE ?', (f"%{genre}%",))
    results = cursor.fetchall()

    conn.close()
    return results

def search_movies_by_rating(min_rating):
    """
    Search for movies in the database by minimum rating.
    Args:
        min_rating: Minimum rating to filter by.
    Returns:
        List of matching rows from the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Use SQL query to filter movies by rating
    cursor.execute('SELECT * FROM movies WHERE rating >= ?', (min_rating,))
    results = cursor.fetchall()

    conn.close()
    return results

if __name__ == "__main__":
    # Load movies from the text file
    movies_from_file = load_movies_from_file()

    print("Search Options:")
    print("1. Search by Title")
    print("2. Search by Genre")
    print("3. Search by Minimum Rating")

    # Get the user's choice
    choice = input("Choose an option (1/2/3): ")

    # Handle the user's choice
    if choice == "1":
        query = input("Enter title to search: ")
        db_results = search_movies_by_title(query)  # Search in the database
        file_results = search_movies_from_file(movies_from_file, query, "title")  # Search in the file
    elif choice == "2":
        query = input("Enter genre to search: ")
        db_results = search_movies_by_genre(query)  # Search in the database
        file_results = search_movies_from_file(movies_from_file, query, "genre")  # Search in the file
    elif choice == "3":
        query = input("Enter minimum rating to search: ")
        db_results = search_movies_by_rating(float(query))  # Search in the database
        file_results = search_movies_from_file(movies_from_file, query, "rating")  # Search in the file
    else:
        print("Invalid choice!")
        db_results = []
        file_results = []

    # Display results from the database
    print("\nSearch Results (From Database):")
    for row in db_results:
        print(row)

    # Display results from the file
    print("\nSearch Results (From File):")
    for movie in file_results:
        print(f"{movie['title']} ({movie['release_year']}) - {movie['genre']} - {movie['rating']}")
