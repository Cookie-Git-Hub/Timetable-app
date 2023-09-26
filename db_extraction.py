import sqlite3

# Создание или подключение к базе данных "schedule.db"
connection = sqlite3.connect("schedule.db")
cursor = connection.cursor()

# Запрос для извлечения расписания из таблицы "Schedule"
cursor.execute('SELECT today, tomorrow, week FROM Schedule')
today_schedule = cursor.fetchone()
tomorrow_schedule = cursor.fetchone()
week_schedule = cursor.fetchone()

def print_today_schedule():
    if today_schedule is not None:
        return today_schedule[0]

def print_tomorrow_schedule():
    if tomorrow_schedule is not None:
        return tomorrow_schedule[0]

def print_week_schedule():
    if week_schedule is not None:
        return week_schedule[0]  

# Закрытие соединения с базой данных
connection.close()
