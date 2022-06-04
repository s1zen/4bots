import sqlite3


async def main():
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()
    
    cursor_db.execute("""CREATE TABLE IF NOT EXISTS bot_support(
                id INT PRIMARY KEY,
                name_btn TEXT,
                link_btn TEXT,
                description TEXT);
    """)
    
    connect_db.commit()
    
    
    if cursor_db.execute("SELECT * FROM bot_support WHERE id = ?", ("1")).fetchone() is None:
        cursor_db.execute("INSERT INTO bot_support VALUES(1, 'test btn', 'https://example.com/', 'Напишите нам если у вас возникли проблемы!')")
        connect_db.commit()

    connect_db.close()