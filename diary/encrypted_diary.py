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

def collect_data():
    the_date = get_date()
    the_time = get_time()
    diary_entry = get_diary_entry()
    stress_level = get_stress_level()
    anxiety = get_anxiety()
    fatigue = get_fatigue()
    pain_level = get_pain_level()
    stoma_bag_change = get_stoma_bag_change()
    leakage = get_leakage()
    medication_taken = get_medication_taken()
    social_work_disruption = get_social_work_disruption()
    sleep_disruption = get_sleep_disruption()
    emotional_state = get_emotional_state()


    return (the_date, the_time, diary_entry, stress_level, anxiety, fatigue,
            pain_level, stoma_bag_change, leakage, medication_taken, social_work_disruption,
            sleep_disruption, emotional_state)

def get_date():
    return datetime.now().strftime('%x')

def get_time():
    return datetime.now().strftime('%H:%M%p')

def get_diary_entry():
    diary_entry = input('Enter diary entry: ')
    return diary_entry

def get_stress_level():
    while True:
        stress_level = input('Enter stress level (0-10): ')
        if stress_level.isdigit() and 0 <= int(stress_level) <= 10:
            return int(stress_level)
        else:
            print('Invalid input. Please enter a number between 0 and 10.')

def get_anxiety():
    while True:
        anxiety = input('Do you feel anxious? (Y/N): ')
        if anxiety.lower() == 'y' or anxiety.lower() == 'n':
            break
        else:
            print('Invalid input. Please enter Y or N.')
    return True if anxiety.lower() == 'y' else False

def get_fatigue():
    while True:
        fatigue = input('Do you feel fatigued? (Y/N): ')
        if fatigue.lower() == 'y' or fatigue.lower() == 'n':
            break
        else:
            print('Invalid input. Please enter Y or N.')
    return True if fatigue.lower() == 'y' else False

def get_pain_level():
    while True:
        pain_level = input('Enter pain level (0-10): ')
        if pain_level.isdigit() and 0 <= int(pain_level) <= 10:
            return int(pain_level)
        else:
            print('Invalid input. Please enter a number between 0 and 10.')

def get_stoma_bag_change():
    while True:
        stoma_bag_change = input('Did you change your stoma bag? (Y/N): ')
        if stoma_bag_change.lower() == 'y' or stoma_bag_change.lower() == 'n':
            break
        else:
            print('Invalid input. Please enter Y or N.')
    return True if stoma_bag_change.lower() == 'y' else False

def get_leakage():
    while True:
        leakage = input('Did you experience leakage? (Y/N): ')
        if leakage.lower() == 'y' or leakage.lower() == 'n':
            break
        else:
            print('Invalid input. Please enter Y or N.')
    return True if leakage.lower() == 'y' else False

def get_medication_taken():
    medication_taken = input('Enter medication taken: ')
    return medication_taken

def get_social_work_disruption():
    while True:
        social_work_disruption = input('Did your stoma cause social/work disruption? (Y/N): ')
        if social_work_disruption.lower() == 'y' or social_work_disruption.lower() == 'n':
            break
        else:
            print('Invalid input. Please enter Y or N.')
    return True if social_work_disruption.lower() == 'y' else False

def get_sleep_disruption():
    while True:
        sleep_disruption = input('Did your stoma cause sleep disruption? (Y/N): ')
        if sleep_disruption.lower() == 'y' or sleep_disruption.lower() == 'n':
            break
        else:
            print('Invalid input. Please enter Y or N.')
    return True if sleep_disruption.lower() == 'y' else False

def get_emotional_state():
    emotional_state = input('Enter emotional state (frustration, depression etc.): ')
    return emotional_state


def insert_data(conn, data):
    pass


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


