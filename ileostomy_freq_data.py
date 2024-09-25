import sqlite3
from datetime import datetime, date, time
from os import system

connection = sqlite3.connect('ileostomy_data_frequency.db')
c = connection.cursor()

def insert_data_entry(the_date = None, the_time = None, amount = None, consistency = None, color = None, ballooning = False,
                      pancaking = False, leakage = False, notes = None):

    c.execute(''' INSERT INTO ileostomy_frequency_log (
              date, time, amount_percent, consistency, color, ballooning, pancaking, leakage, notes)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
              ''', (the_date, the_time, amount, consistency, color,
                     ballooning, pancaking, leakage, notes))
    
    connection.commit()
    print('Entry added')



def get_date():
    today_date = datetime.now()
    while True:
        q = input("Are you inputting data for todays date? (Y/N) ")
        if q == "Y" or q == "y":
            print(q)
            return today_date.strftime("%x")
        elif q == "N" or q == "n":
            while True:
                not_today = input("Please enter the day and month in this format: 'day:month' example = '24:5' : ")
                if ':' in not_today:
                    d_m_split = not_today.split(':')
                    try:
                        new_date = date(int(today_date.strftime("%G")), int(d_m_split[1]), int(d_m_split[0]))
                        return new_date
                    except ValueError:
                        print("Invalid day or month. Please try again. ")
                else:
                    print("Please try again in the correct format - day:month : ")
        else:
            print("Invalid input. Please enter Y or N")

def get_time():
    # the_time = datetime.now().strftime("%I:%M%p")
    while True:
        current_time = input("Are you inputting data for the current time? (Y/N) ")
        if current_time == "Y" or current_time == "y":
            return datetime.now().strftime("%I:%M%p")
        elif current_time == "N" or current_time == "n":
            while True:
                t_input = input('Please enter the data time in this format: hour:minute (example = 23:44) : ')
                if ':' in t_input:
                    t_split = t_input.split(':')
                    try:
                        new_time = time(int(t_split[0]), int(t_split[1]), 0)
                        return new_time.strftime('%I:%M%p')
                    except ValueError:
                        print('Invalid Input. Please try again.')
                else:
                    print('Invalid input. Please try again: ')           
        else:
            print("Invalid input. Please enter Y or N")
        

def get_amount():
    while True:
        try:
            answer = int(input('How full was your stoma? (0-100) : '))
            if answer >= 0 and answer <= 100:
                return answer
            else:
                print('Invalid input. Please try again.')
        except ValueError:
            print('Please enter a number.')

def get_consistency():
    while True:
        try:
            answer = int(input('1 being watery and 10 being solid, what was the consistency of your stoma? '))
            if 1 <= answer <= 10:
                return answer
            else:
                print('Invalid input. Please try again')
        except ValueError:
            print('Please enter a number from 1-10')

def get_color():
        answer = input('What color was the output? ')
        return answer.title()

def get_boolean(var):
    while True:
        answer = input(f'Was there any {var}? (Y/N) : ')
        if answer == 'Y' or answer == "y":
            return True
        elif answer == "N" or answer == 'n':
            return False
        else:
            print("Invalid input. Please enter Y or N")

def get_notes():
    answer = input('Any additional notes? : ')
    return answer.capitalize()

def clear_terminal():
    return system('clear')

clear_terminal()
getting_date = get_date()
clear_terminal()
getting_time = get_time()
clear_terminal()
getting_amount = get_amount()
clear_terminal()
getting_consistency = get_consistency()
clear_terminal()
getting_color = get_color()
clear_terminal()
getting_ballooning = get_boolean('Ballooning')
clear_terminal()
getting_pancaking = get_boolean('Pancaking')
clear_terminal()
getting_leakage = get_boolean('Leakage')
clear_terminal()
getting_notes = get_notes()
clear_terminal()

insert_data_entry(getting_date, getting_time, getting_amount, getting_consistency, getting_color,
                  getting_ballooning, getting_pancaking, getting_leakage, getting_notes)
