from dotenv import load_dotenv
import os
import logging

from scripts.search_movies import (
    search_movies_by_title,
    search_movies_by_genre,
    search_movies_by_rating,
    load_movies_from_file,
    search_movies_from_file
)
from scripts.add_movie import add_movie
from scripts.scrape_movies import scrape_movie_details

# Load environment variables
load_dotenv()

# Get paths from environment variables
DB_PATH = os.getenv("DB_PATH", "database/movies.db")
MOVIES_FILE = os.getenv("MOVIES_FILE", "scripts/top_250_movies.txt")
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")

# Ensure the logs directory exists
log_dir = os.path.dirname(LOG_FILE)
if log_dir and not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Application started.")

    print("Options:")
    print("1. Search Movies")
    print("2. Add Movie")
    print("3. Scrape Movie Details")

    choice = input("Choose an option: ")

    if choice == "1":
        search_type = input("Search by (title/genre/rating): ").strip().lower()
        if search_type not in ["title", "genre", "rating"]:
            print("Invalid search type! Please choose from 'title', 'genre', or 'rating'.")
        else:
            query = input("Enter your search query: ").strip()
            print(f"DEBUG: Search Type: {search_type}, Query: {query}")  # Debugging line

            movies_from_file = load_movies_from_file()
            if search_type == "title":
                db_results = search_movies_by_title(query)
                file_results = search_movies_from_file(movies_from_file, query, "title")
            elif search_type == "genre":
                db_results = search_movies_by_genre(query)
                file_results = search_movies_from_file(movies_from_file, query, "genre")
            elif search_type == "rating":
                db_results = search_movies_by_rating(float(query))
                file_results = search_movies_from_file(movies_from_file, query, "rating")

            print("\nSearch Results (From Database):")
            for row in db_results:
                print(row)

            print("\nSearch Results (From File):")
            for movie in file_results:
                print(f"{movie['title']} ({movie['release_year']}) - {movie['genre']} - {movie['rating']}")

    elif choice == "2":
        title = input("Enter movie title: ")
        genre = input("Enter movie genre: ")
        release_year = int(input("Enter release year: "))
        rating = float(input("Enter movie rating: "))
        add_movie(title, genre, release_year, rating)

    elif choice == "3":
        movie_url = input("Enter IMDb movie URL: ")
        details = scrape_movie_details(movie_url)
        print("\nScraped Movie Details:")
        print(details)

    else:
        print("Invalid choice!")

    logging.info("Application finished.")

if __name__ == "__main__":
    main()
