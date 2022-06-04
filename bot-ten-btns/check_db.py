import sqlite3

async def main():
    connect_db = sqlite3.connect("../db/bots.db")
    cursor_db = connect_db.cursor()
    
    cursor_db.execute("""CREATE TABLE IF NOT EXISTS bot_ten_btns (
                id INT PRIMARY KEY,
                name_btn TEXT,
                link_btn TEXT,
                description TEXT);
    """)
    
    connect_db.commit()
    
    total = 0
    for i in range(1, 11 + 1):
        if total == 10 and cursor_db.execute(f"SELECT * FROM bot_ten_btns WHERE id = {i}").fetchone() is None:
            cursor_db.execute(f"INSERT INTO bot_ten_btns VALUES({i}, '', '', 'test desc')")
            connect_db.commit()
            
        if cursor_db.execute(f"SELECT * FROM bot_ten_btns WHERE id = {i}").fetchone() is None:
            cursor_db.execute(f"INSERT INTO bot_ten_btns VALUES({i}, 'test btn{i}', 'https://example.com/{i}', '')")
            connect_db.commit() 
        total += 1
        
    connect_db.close()