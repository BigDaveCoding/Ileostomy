import datetime
import os
import sqlite3

def connect_to_db(db_name):
    # Connect to the database
    conn = sqlite3.connect(db_name)
    return conn