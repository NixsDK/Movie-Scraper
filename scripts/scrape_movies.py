import os
import sqlite3
import time
from playwright.sync_api import sync_playwright

# Path to the SQLite database
DB_PATH = "database/movies.db"

def scrape_movie_details(movie_url):
    """Scrape movie details from an IMDb URL."""
    with sync_playwright() as p:
        # Launch the browser in headless mode
        browser = p.chromium.launch(headless=True)
        
        # Create a new browser context with a custom user agent
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        
        # Open a new page and navigate to the provided URL
        page = context.new_page()
        page.goto(movie_url)
        time.sleep(5)  # Wait for the page to load completely

        # Initialize variables to store scraped data
        try:
            # Extract the movie title
            title = page.query_selector("h1").inner_text() if page.query_selector("h1") else "Unknown Title"
        except:
            title = "Unknown Title"

        try:
            # Extract movie genres as a list
            genres = page.locator("span.ipc-chip__text").all_inner_texts() if page.locator("span.ipc-chip__text") else ["Unknown Genre"]
        except:
            genres = ["Unknown Genre"]

        try:
            # Extract the release year using a specific link structure
            release_year_element = page.query_selector("a.ipc-link--baseAlt[href*='/releaseinfo']")
            release_year = release_year_element.inner_text() if release_year_element else "Unknown Year"
        except:
            release_year = "Unknown Year"

        try:
            # Extract the movie rating
            rating_element = page.query_selector("span.sc-d541859f-1.imUuxf")
            rating = rating_element.inner_text() if rating_element else "Rating not available"
        except:
            rating = "Rating not available"

        # Debug print to check the scraped data
        print(f"Scraped Data - Title: {title}, Genres: {genres}, Year: {release_year}, Rating: {rating}")

        # Close the browser
        browser.close()

        # Return the scraped data as a dictionary
        return {
            "title": title,
            "genres": genres,
            "release_year": release_year,
            "rating": rating
        }

def save_movie_to_db(movie):
    """Save the scraped movie details into the SQLite database."""
    # Check if the database file exists
    if not os.path.exists(DB_PATH):
        print("Database not found. Please run setup_database.py first.")
        return

    # Connect to the SQLite database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        # Insert the movie details into the movies table
        cursor.execute('''
            INSERT INTO movies (title, genre, release_year, rating)
            VALUES (?, ?, ?, ?)
        ''', (
            movie["title"],
            ", ".join(movie["genres"]),  # Convert genres list to a comma-separated string
            int(movie["release_year"]) if movie["release_year"].isdigit() else None,
            float(movie["rating"]) if movie["rating"] != "Rating not available" else None
        ))
        conn.commit()  # Save the changes
        print(f"Movie '{movie['title']}' added to the database.")
    except sqlite3.Error as e:
        # Handle database errors
        print(f"Error saving movie to database: {e}")
    finally:
        conn.close()  # Close the database connection

if __name__ == "__main__":
    # List of IMDb movie URLs to scrape
    movie_urls = [
        "https://www.imdb.com/title/tt10366206/",  # John Wick: Chapter 4
        "https://www.imdb.com/title/tt0468569/",  # The Dark Knight
        "https://www.imdb.com/title/tt0120737/",  # The Fellowship of the Ring
        "https://www.imdb.com/title/tt0172495/",  # Gladiator
        "https://www.imdb.com/title/tt4154756/",  # Avengers: Infinity War
        "https://www.imdb.com/title/tt7286456/"   # Joker
    ]

    for url in movie_urls:
        # Print the URL being scraped
        print(f"Scraping: {url}")
        
        # Scrape movie details and save them to the database
        movie_data = scrape_movie_details(url)
        if movie_data:
            save_movie_to_db(movie_data)
        
        # Pause between requests to avoid overloading the server
        time.sleep(2)
