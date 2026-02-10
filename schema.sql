CREATE TABLE books (
     id INTEGER PRIMARY KEY,
     title TEXT NOT NULL,
     author TEXT NOT NULL,
     pages INTEGER,
     genre TEXT,
     status TEXT CHECK(status IN('reading', 'want', 'read')),
     started_date DATE,
     finished_date DATE,
     rating INTEGER CHECK(rating BETWEEN 1 AND 5),
     notes TEXT,
     UNIQUE(title, author)
);

CREATE TABLE reading_sessions (
    id INTEGER PRIMARY KEY,
    book_id INTEGER NOT NULL,
    session_date DATE NOT NULL,
    pages_read INTEGER,
    minutes_read INTEGER,
    FOREIGN KEY (book_id) REFERENCES books(id)
);
