import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('ileostomy_data_frequency.db')
df = pd.read_sql_query("SELECT * FROM ileostomy_frequency_log", conn)


# Checking for null values
if df.isnull().values.any():
    print("There are null values in the DataFrame")
    print(df[df.isnull().any(axis=1)])
    df.dropna(axis=0, how='any', inplace=True)
else:
    print("There are no null values in the DataFrame")

# Print descriptive statistics
print(df.describe())
