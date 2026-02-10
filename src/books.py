from src.db import get_connection

def add_book(title, author, pages=None, genre=None, status="want"):
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT id FROM books WHERE title = ? AND author = ?", (title, author))
    existing = c.fetchone()

    if existing: 
        conn.close()
        return existing[0]

    c.execute("""INSERT INTO books(title, author, pages, genre, status) VALUES (?, ?, ?, ?, ?)""", (title, author, pages, genre, status))
    
    book_id = c.lastrowid
    conn.commit()
    conn.close()
    return book_id

def list_books():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    rows = c.fetchall()
    conn.close()
    return rows