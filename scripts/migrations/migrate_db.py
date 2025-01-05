import os
import logging
import sqlite3
import time
from datetime import datetime

# Ensure the logs directory exists
LOG_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../logs/app.log'))
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# Configure logging directly
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger('root')

DB_PATH = os.getenv("DB_PATH", "database/movies.db")
logger.info('SQLite DB migration service initialized')

# Establish database connection
connection = None

def init_db():
    global connection
    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to SQLite DB at {DB_PATH}")
    except sqlite3.Error as e:
        logger.error(f"Error connecting to SQLite DB: {e}")
        raise

def get_cursor():
    global connection
    if connection is None:
        init_db()
    return connection.cursor()

# Check if table exists
def sqlite_check_if_table_exists(table_name):
    cursor = get_cursor()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    return cursor.fetchone() is not None

# Create migrations table
def sqlite_create_migrations_table():
    cursor = get_cursor()
    try:
        cursor.execute("""
            CREATE TABLE migrations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                exec_ts INTEGER NOT NULL,
                exec_dt TEXT NOT NULL
            )
        """)
        connection.commit()
        logger.info("Migrations table created")
    except sqlite3.Error as e:
        logger.error(f"Error creating migrations table: {e}")
        raise

# Check if migration exists
def sqlite_check_if_migration_exists(migration_name):
    cursor = get_cursor()
    cursor.execute("SELECT COUNT(*) FROM migrations WHERE name = ?", (migration_name,))
    return cursor.fetchone()[0] > 0

# Execute SQL queries
def sqlite_exec_sql(sql_query):
    cursor = get_cursor()
    try:
        cursor.executescript(sql_query)
        connection.commit()
        logger.info("SQL executed successfully")
        return True
    except sqlite3.Error as e:
        logger.error(f"Error executing SQL: {sql_query}\n{e}")
        return False

# Insert migration record
def sqlite_insert_migration(name, exec_ts, exec_dt):
    cursor = get_cursor()
    try:
        cursor.execute("INSERT INTO migrations (name, exec_ts, exec_dt) VALUES (?, ?, ?)", (name, exec_ts, exec_dt))
        connection.commit()
        logger.info(f"Migration '{name}' recorded in database")
    except sqlite3.Error as e:
        logger.error(f"Error recording migration: {e}")
        raise

# Ensure migrations table exists
if not sqlite_check_if_table_exists("migrations"):
    sqlite_create_migrations_table()

# Process migration files
migrations_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
migrations_files = [f for f in os.listdir(migrations_dir) if f.endswith('.sql')]
print("DEBUG: Detected Migration Files:", migrations_files)  # Debugging

migrations_files.sort()


print("DEBUG: Detected Migration Files:", migrations_dir)  # Add this line

migrations_applied = 0

for migration in migrations_files:
    print(f"DEBUG: Processing {migration}")  # Add this line
    if not sqlite_check_if_migration_exists(migration):
        logger.info(f"Applying migration: {migration}")
        with open(os.path.join(migrations_dir, migration), 'r') as file:
            sql = file.read()
        if sqlite_exec_sql(sql):
            exec_ts = int(time.time())
            exec_dt = datetime.fromtimestamp(exec_ts).strftime('%Y-%m-%d %H:%M:%S')
            sqlite_insert_migration(migration, exec_ts, exec_dt)
            migrations_applied += 1
        else:
            logger.error(f"Migration failed: {migration}")
            break


if migrations_applied == 0:
    logger.info("No new migrations to apply")
else:
    logger.info(f"{migrations_applied} migrations applied successfully")
