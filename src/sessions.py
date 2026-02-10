import sqlite3
from src.db import get_connection
from datetime import date

def log_reading(book_id, pages_read, minutes_read, session_date=None):
    session_date = session_date or date.today().isoformat()
    conn = get_connection()
    c = conn.cursor()
    c.execute("""INSERT INTO reading_sessions(book_id, session_date, pages_read, minutes_read) VALUES (?, ?, ?, ?)""", (book_id, session_date, pages_read, minutes_read))
    conn.commit()
    conn.close()

def get_book_progress(book_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""SELECT SUM(pages_read) as total_pages, SUM(minutes_read) as total_minutes FROM reading_sessions WHERE book_id=?""", (book_id))
    result = c.fetchone()
    conn.close()
    return result