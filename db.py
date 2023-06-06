import sqlite3

conn = sqlite3.connect('books.sqlite')
cursor = conn.cursor()
sql_query = """CREATE TABLE IF NOT EXISTS books (    
    id integer PRIMARY KEY,    
    title text NOT NULL,    
    author text NOT NULL,    
    language text NOT NULL    
    )"""

cursor.execute(sql_query)
