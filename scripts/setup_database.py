import sqlite3
import os

def setup_database():
    db_folder = "database"
    db_path = os.path.join(db_folder, "movies.db")

    # Ensure the database folder exists
    os.makedirs(db_folder, exist_ok=True)

    # Connect to the database, which creates it if it doesn't exist
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the movies table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT,
            release_year INTEGER,
            rating REAL
        )
    ''')

    # Create the migrations table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            exec_ts INTEGER NOT NULL,
            exec_dt TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Database setup completed. Database path: {db_path}")

def check_migrations_table():
    """Check and display the contents of the migrations table."""
    db_path = "database/movies.db"

    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}. Please run the migration script first.")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM migrations")
        rows = cursor.fetchall()

        if rows:
            print("Applied Migrations:")
            for row in rows:
                print(row)
        else:
            print("No migrations applied.")
    except sqlite3.Error as e:
        print(f"Error querying migrations table: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    print("Options:")
    print("1. Setup Database")
    print("2. Check Migrations")

    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        setup_database()
    elif choice == "2":
        check_migrations_table()
    else:
        print("Invalid option.")
