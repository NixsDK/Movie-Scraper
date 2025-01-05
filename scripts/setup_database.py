import sqlite3
import os

def setup_database():
    """
    Set up the SQLite database by ensuring the database folder and file exist, 
    and creating necessary tables (movies and migrations) if they do not already exist.
    """
    db_folder = "database"  # Directory where the database will be stored
    db_path = os.path.join(db_folder, "movies.db")  # Full path to the database file

    # Ensure the database folder exists, create it if it doesn't
    os.makedirs(db_folder, exist_ok=True)

    # Connect to the database; creates the file if it doesn't exist
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the 'movies' table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each movie
            title TEXT NOT NULL,                  -- Movie title (required)
            genre TEXT,                           -- Genre(s) of the movie
            release_year INTEGER,                 -- Year of release
            rating REAL                           -- Movie rating
        )
    ''')

    # Create the 'migrations' table to track applied migrations
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS migrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique ID for each migration
            name TEXT NOT NULL,                   -- Name of the migration file
            exec_ts INTEGER NOT NULL,            -- Timestamp when migration was applied
            exec_dt TEXT NOT NULL                -- Datetime when migration was applied
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    # Print confirmation of database setup
    print(f"Database setup completed. Database path: {db_path}")

def check_migrations_table():
    """
    Check and display the contents of the migrations table to show applied migrations.
    """
    db_path = "database/movies.db"  # Path to the database file

    # Check if the database file exists
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}. Please run the migration script first.")
        return

    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        # Query the migrations table to fetch all rows
        cursor.execute("SELECT * FROM migrations")
        rows = cursor.fetchall()

        # Display applied migrations if any exist
        if rows:
            print("Applied Migrations:")
            for row in rows:
                print(row)  # Print each migration record
        else:
            print("No migrations applied.")
    except sqlite3.Error as e:
        # Handle errors during the query
        print(f"Error querying migrations table: {e}")
    finally:
        # Ensure the connection is closed
        conn.close()

if __name__ == "__main__":
    # Display menu options to the user
    print("Options:")
    print("1. Setup Database")       # Option to set up the database and tables
    print("2. Check Migrations")     # Option to check the applied migrations

    # Get user choice
    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        # Run the setup database function
        setup_database()
    elif choice == "2":
        # Run the function to check migrations table
        check_migrations_table()
    else:
        # Handle invalid options
        print("Invalid option.")
