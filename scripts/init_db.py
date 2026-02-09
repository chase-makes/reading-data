import sqlite3

conn = sqlite3.connect("data/books.db")

with open("schema.sql") as f:
    conn.executescript(f.read())

conn.close()
print("Database initialized")
