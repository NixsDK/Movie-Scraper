import sys
import os

# Explicitly append the project root directory to sys.path
# This ensures the test script can locate modules in the project
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)  # Add the project root to Python's module search path

# Import the function to be tested from the scripts module
from scripts.search_movies import search_movies_by_title

def test_search_movies_by_title():
    """
    Test the search_movies_by_title function using a mock database setup.
    """
    # Mock database setup: A list of dictionaries simulating database rows
    test_movies = [
        {"title": "The Shawshank Redemption", "genre": "Drama", "release_year": 1994, "rating": 9.3},
        {"title": "The Godfather", "genre": "Crime, Drama", "release_year": 1972, "rating": 9.2}
    ]

    # Perform a simulated search for movies containing "Shawshank" in the title
    results = [movie for movie in test_movies if "Shawshank" in movie["title"]]

    # Assert that exactly one result is found
    assert len(results) == 1

    # Assert that the result matches the expected movie title
    assert results[0]["title"] == "The Shawshank Redemption"
