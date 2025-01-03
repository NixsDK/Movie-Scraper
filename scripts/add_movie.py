import sqlite3

DB_PATH = "database/movies.db"

def add_movie(title, genre, release_year, rating):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO movies (title, genre, release_year, rating)
        VALUES (?, ?, ?, ?)
    ''', (title, genre, release_year, rating))

    conn.commit()
    conn.close()
    print(f"Movie '{title}' added to the database.")

if __name__ == "__main__":
    title = input("Enter movie title: ")
    genre = input("Enter movie genre: ")
    release_year = int(input("Enter release year: "))
    rating = float(input("Enter movie rating: "))

    add_movie(title, genre, release_year, rating)
