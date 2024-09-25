import sqlite3
import json
from datetime import datetime, date, time

def connect_to_db(db_name, passphrase):
    conn = sqlite3.connect(db_name)
    conn.execute(f"PRAGMA key = '{passphrase}'")
    return conn

def create_table(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS stoma_diary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            diary_entry TEXT NOT NULL,
            stress_level INTEGER NOT NULL,
            anxiety BOOLEAN NOT NULL,
            fatigue BOOLEAN NOT NULL,
            pain_level INTEGER NOT NULL,
            stoma_bag_change BOOLEAN NOT NULL,
            leakage BOOLEAN NOT NULL,
            medication_taken TEXT NOT NULL,
            social_work_disruption BOOLEAN NOT NULL,
            sleep_disruption BOOLEAN NOT NULL,
            emotional_state TEXT NOT NULL
        )
    ''')
    conn.commit()

def main():
    db_name = 'encrypted_diary.db'
    
    # Load passphrase from config file
    with open('passphrase.json', 'r') as config_file:
        config = json.load(config_file)
        passphrase = config['encrypted_diary_passphrase']

    conn = connect_to_db(db_name, passphrase)
    create_table(conn)

if __name__ == '__main__':
    main()


