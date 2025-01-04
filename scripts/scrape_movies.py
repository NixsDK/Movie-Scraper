import os
import sqlite3
import time
from playwright.sync_api import sync_playwright

DB_PATH = "database/movies.db"

def scrape_movie_details(movie_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        page = context.new_page()
        page.goto(movie_url)
        time.sleep(5)

        # Scrape movie details
        try:
            title = page.query_selector("h1").inner_text() if page.query_selector("h1") else "Unknown Title"
        except:
            title = "Unknown Title"

        try:
            genres = page.locator("span.ipc-chip__text").all_inner_texts() if page.locator("span.ipc-chip__text") else ["Unknown Genre"]
        except:
            genres = ["Unknown Genre"]

        try:
            release_year_element = page.query_selector("a.ipc-link--baseAlt[href*='/releaseinfo']")
            release_year = release_year_element.inner_text() if release_year_element else "Unknown Year"
        except:
            release_year = "Unknown Year"

        try:
            rating_element = page.query_selector("span.sc-d541859f-1.imUuxf")
            rating = rating_element.inner_text() if rating_element else "Rating not available"
        except:
            rating = "Rating not available"

        # Debug print for scraped data
        print(f"Scraped Data - Title: {title}, Genres: {genres}, Year: {release_year}, Rating: {rating}")

        browser.close()

        return {
            "title": title,
            "genres": genres,
            "release_year": release_year,
            "rating": rating
        }

def save_movie_to_db(movie):
    if not os.path.exists(DB_PATH):
        print("Database not found. Please run setup_database.py first.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO movies (title, genre, release_year, rating)
            VALUES (?, ?, ?, ?)
        ''', (
            movie["title"],
            ", ".join(movie["genres"]),
            int(movie["release_year"]) if movie["release_year"].isdigit() else None,
            float(movie["rating"]) if movie["rating"] != "Rating not available" else None
        ))
        conn.commit()
        print(f"Movie '{movie['title']}' added to the database.")
    except sqlite3.Error as e:
        print(f"Error saving movie to database: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    movie_urls = [
        "https://www.imdb.com/title/tt10366206/",  #  John Wick: Chapter 4
        "https://www.imdb.com/title/tt0468569/",  #  The Dark Knight
        "https://www.imdb.com/title/tt0120737/",   #  The Fellowship of the Ring
        "https://www.imdb.com/title/tt0172495/", # Gladiator
        "https://www.imdb.com/title/tt4154756/", # Avengers: Infinity War
        "https://www.imdb.com/title/tt7286456/" # Joker
    ]

    for url in movie_urls:
        print(f"Scraping: {url}")
        movie_data = scrape_movie_details(url)
        if movie_data:
            save_movie_to_db(movie_data)
        time.sleep(2)  # Be polite to the server
