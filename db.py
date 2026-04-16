import psycopg2
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS trips (
        id INT,
        mail TEXT,
        name TEXT,
        departure TEXT,
        destination TEXT,
        start_date TIMESTAMP,
        end_date TIMESTAMP
    )
    """)

    conn.commit()
    cur.close()
    conn.close()

def insert_data(data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO trips VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (
        data['id'],
        data['mail'],
        data['name'],
        data['trip']['departure'],
        data['trip']['destination'],
        data['trip']['start_date'],
        data['trip']['end_date']
    ))

    conn.commit()
    cur.close()
    conn.close()
