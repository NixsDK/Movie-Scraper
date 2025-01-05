import sqlite3
import os

# Path to the SQLite database file
DB_PATH = "database/movies.db"

# Path to the file containing movie details
MOVIES_FILE = "scripts/movies.txt"

def add_movie(title, genre, release_year, rating):
    """
    Add a single movie to the database.
    Args:
        title (str): The title of the movie.
        genre (str): The genre of the movie.
        release_year (int): The release year of the movie.
        rating (float): The rating of the movie.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Insert the movie details into the 'movies' table
    cursor.execute('''
        INSERT INTO movies (title, genre, release_year, rating)
        VALUES (?, ?, ?, ?)
    ''', (title, genre, release_year, rating))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Confirm that the movie was added successfully
    print(f"Movie '{title}' added to the database.")

def add_movies_from_file(file_path):
    """
    Add multiple movies to the database from a file.
    Args:
        file_path (str): The path to the file containing movie details.
    """
    # Check if the specified file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Skip empty lines or lines starting with a comment
            if not line.strip() or line.startswith("#"):
                continue

            # Parse the line and add the movie to the database
            try:
                title, genre, release_year, rating = line.strip().split('|')
                add_movie(title, genre, int(release_year), float(rating))
            except ValueError as e:
                # Handle parsing errors gracefully
                print(f"Skipping line due to parsing error: {line.strip()} ({e})")

if __name__ == "__main__":
    # Display options for the user
    print("1. Add a single movie")
    print("2. Add movies from file")

    # Get the user's choice
    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        # Handle adding a single movie
        title = input("Enter movie title: ")  # Get movie title from user
        genre = input("Enter movie genre: ")  # Get movie genre from user
        release_year = int(input("Enter release year: "))  # Get release year
        rating = float(input("Enter movie rating: "))  # Get movie rating
        add_movie(title, genre, release_year, rating)

    elif choice == "2":
        # Handle adding movies from a file
        add_movies_from_file(MOVIES_FILE)

    else:
        # Handle invalid menu choices
        print("Invalid choice. Exiting.")
