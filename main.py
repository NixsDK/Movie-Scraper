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

# Load environment variables from a .env file
load_dotenv()

# Retrieve paths and file configurations from environment variables
DB_PATH = os.getenv("DB_PATH", "database/movies.db")  # Path to the SQLite database
MOVIES_FILE = os.getenv("MOVIES_FILE", "scripts/top_250_movies.txt")  # Path to the file with top 250 movies
LOG_FILE = os.getenv("LOG_FILE", "logs/app.log")  # Path to the log file

# Ensure the logs directory exists, creating it if necessary
log_dir = os.path.dirname(LOG_FILE)
if log_dir and not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logging to write logs to the specified file
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # Log level: INFO
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log message format
)

def main():
    """
    Main function to interact with the user for movie management operations.
    Provides options to search, add, or scrape movie details.
    """
    logging.info("Application started.")  # Log the start of the application

    # Display menu options
    print("Options:")
    print("1. Search Movies")  # Option to search movies by various criteria
    print("2. Add Movie")  # Option to add a new movie to the database
    print("3. Scrape Movie Details")  # Option to scrape movie details from IMDb

    # Get the user's choice
    choice = input("Choose an option: ")

    if choice == "1":
        # Handle movie search
        search_type = input("Search by (title/genre/rating): ").strip().lower()
        if search_type not in ["title", "genre", "rating"]:
            # Validate search type
            print("Invalid search type! Please choose from 'title', 'genre', or 'rating'.")
        else:
            # Get the user's query
            query = input("Enter your search query: ").strip()
            print(f"DEBUG: Search Type: {search_type}, Query: {query}")  # Debugging information

            # Load movies from file
            movies_from_file = load_movies_from_file()

            # Perform the search based on the selected type
            if search_type == "title":
                db_results = search_movies_by_title(query)
                file_results = search_movies_from_file(movies_from_file, query, "title")
            elif search_type == "genre":
                db_results = search_movies_by_genre(query)
                file_results = search_movies_from_file(movies_from_file, query, "genre")
            elif search_type == "rating":
                db_results = search_movies_by_rating(float(query))
                file_results = search_movies_from_file(movies_from_file, query, "rating")

            # Display search results from the database
            print("\nSearch Results (From Database):")
            for row in db_results:
                print(row)

            # Display search results from the file
            print("\nSearch Results (From File):")
            for movie in file_results:
                print(f"{movie['title']} ({movie['release_year']}) - {movie['genre']} - {movie['rating']}")

    elif choice == "2":
        # Handle adding a new movie
        title = input("Enter movie title: ")
        genre = input("Enter movie genre: ")
        release_year = int(input("Enter release year: "))
        rating = float(input("Enter movie rating: "))
        add_movie(title, genre, release_year, rating)  # Add movie to the database

    elif choice == "3":
        # Handle scraping movie details
        movie_url = input("Enter IMDb movie URL: ")
        details = scrape_movie_details(movie_url)  # Scrape movie details from the URL
        print("\nScraped Movie Details:")
        print(details)

    else:
        # Handle invalid menu choice
        print("Invalid choice!")

    logging.info("Application finished.")  # Log the end of the application

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
