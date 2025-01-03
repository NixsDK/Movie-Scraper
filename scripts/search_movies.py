import sqlite3

DB_PATH = "database/movies.db"

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
    print("Search Options:")
    print("1. Search by Title")
    print("2. Search by Genre")
    print("3. Search by Minimum Rating")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        title = input("Enter title to search: ")
        results = search_movies_by_title(title)
    elif choice == "2":
        genre = input("Enter genre to search: ")
        results = search_movies_by_genre(genre)
    elif choice == "3":
        min_rating = float(input("Enter minimum rating: "))
        results = search_movies_by_rating(min_rating)
    else:
        print("Invalid choice!")
        results = []

    print("\nSearch Results:")
    for row in results:
        print(row)
