import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('personal.db')
cursor = conn.cursor()

# Select all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Drop each table
for table_name in tables:
        print(f"Deleting: {table_name[0]}")
        try:
            cursor.execute(f"DROP TABLE IF EXISTS {table_name[0]}")
        except:
            pass

# Commit changes and close connection

cursor.execute(f"DROP TABLE IF EXISTS {table_name[0]}")

conn.commit()
conn.close()
