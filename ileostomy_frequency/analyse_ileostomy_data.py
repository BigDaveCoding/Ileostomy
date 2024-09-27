import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
print('Descriptive statistics for the DataFrame')
print(df.describe(include='all'))

print('value_counts for specific columns')
print(df['consistency'].value_counts())
print('Unique values for consistency : ' + str(df['consistency'].unique()))
print(df['amount_percent'].value_counts())

print(df.head(1))

def plot_histogram(column_name):
    # Testing a histogram
    unique_vals = df[column_name].unique()
    bins = np.arange(min(unique_vals) - 0.5, max(unique_vals) + 1.5, 1)
    df[column_name].hist(bins=bins, color='green', edgecolor='black', rwidth=0.8)
    plt.title(f'Histogram of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')

    max_x = df[column_name].max()

    match max_x:
        case x if 0 <= x <= 10:
            plt.xticks(np.arange(0, max_x + 1, 1))
        case x if 10 < x <= 100:
            plt.xticks(np.arange(0, max_x + 5, 5))
        case x if x > 100:
            print('Error')
        case _:
            print('unknown case')
    
    # plt.xticks(np.arange(0, max_x + 5, 5))
    max_y = df[column_name].value_counts().max()
    plt.yticks(np.arange(0, max_y + 1, 1))
    plt.show()

# print(plot_histogram('amount_percent'))
# print(plot_histogram('consistency'))

def overlay_hist(column_list):
    num_columns = len(column_list)
    width = 0.8 / num_columns

    for column in column_list:
        unique_vals = df[column].unique()
        bins = np.arange(min(unique_vals) - 0.5, max(unique_vals) + 1.5, 1)
        df[column].hist(bins=bins, alpha=0.5, label=column, edgecolor='black', rwidth=width)

    max_x = max(df[column].max() for column in column_list)
    plt.xticks(np.arange(0, max_x + 1, 1))
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Overlay Histogram')
    plt.legend()
    plt.show()

print(overlay_hist(['amount_percent', 'consistency']))

# df['consistency'].plot(kind='density', label='consistency')
# df['amount_percent'].plot(kind='density', label='amount')
# plt.title('Density plot of consistency & amount_percent')
# plt.xlabel('Consistency')
# plt.ylabel('Density')
# plt.legend()
# plt.show()