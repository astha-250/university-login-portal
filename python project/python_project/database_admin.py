import sqlite3

DB_ADMIN = "adminsql.db"

def setup_database():
    conn = sqlite3.connect(DB_ADMIN)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS admins (
        name TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    admin_records=[
        ('Srihari Mandava','sri@vit'),
        ('Arun Prasath G','aru@vit'),
        ('Jaganatha Pandian B','jag@vit'),
        ('Animesh Roy','ani@vit'),
        ('Thenmozhi K','the@vit'),
    ]
    
    cursor.execute("SELECT COUNT(*) FROM admins")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
        INSERT INTO admins (name,password) VALUES (?, ?)
        ''', admin_records)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database_admin setup complete.")
