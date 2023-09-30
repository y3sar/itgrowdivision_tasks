# database.py
import sqlite3

conn = sqlite3.connect('social_network.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        bio TEXT
    )
''')
conn.commit()
