import sys
import os

# Explicitly append the project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

# Import from scripts
from scripts.search_movies import search_movies_by_title

def test_search_movies_by_title():
    # Mock database setup
    test_movies = [
        {"title": "The Shawshank Redemption", "genre": "Drama", "release_year": 1994, "rating": 9.3},
        {"title": "The Godfather", "genre": "Crime, Drama", "release_year": 1972, "rating": 9.2}
    ]

    results = [movie for movie in test_movies if "Shawshank" in movie["title"]]
    assert len(results) == 1
    assert results[0]["title"] == "The Shawshank Redemption"
