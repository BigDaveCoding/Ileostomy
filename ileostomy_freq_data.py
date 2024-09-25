import sqlite3
from datetime import datetime, date

connection = sqlite3.connect('ileostomy_data_frequency.db')
c = connection.cursor()

def insert_data_entry(the_date = None, the_time = None, amount = None, consistency = None, color = None, ballooning = False,
                      pancaking = False, leakage = False, notes = None):

    c.execute(''' INSERT INTO ileostomy_data_frequency (
              date, time, amount, consistency, color, ballooning, pancaking, leakage, notes)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
              '''), (the_date, the_time, amount, consistency, color,
                     ballooning, pancaking, leakage, notes)
    
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
    time = datetime.now().strftime("%I:%M%p")
    return time
        
    
        
                    
            

        

    
# getting_date = get_date()
# print(getting_date)
getting_time = get_time()
print(getting_time)




    
