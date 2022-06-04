import sqlite3


async def main():
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()
    
    cursor_db.execute("""CREATE TABLE IF NOT EXISTS botOneBtn(
                id INT PRIMARY KEY,
                name_btn TEXT,
                link_btn TEXT,
                description TEXT);
    """)
    
    connect_db.commit()
    
    
    if cursor_db.execute("SELECT * FROM botOneBtn WHERE id = ?", ("1")).fetchone() is None:
        cursor_db.execute("INSERT INTO botOneBtn VALUES(1, 'test btn', 'https://example.com/', 'test desc')")
        connect_db.commit()

    connect_db.close()