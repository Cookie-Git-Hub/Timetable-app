import sqlite3
from functions.today import perform_parsing_today
from functions.tomorrow import perform_parsing_tomorrow
from functions.week import perform_parsing_week

# Создание или подключение к базе данных "schedule.db"
connection = sqlite3.connect("db/schedule.db")
cursor = connection.cursor()

# Создание таблицы Schedule, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS schedule (
    today TEXT NOT NULL,
    tomorrow TEXT NOT NULL,
    week TEXT NOT NULL
)
''')

# Получение данных для вставки
today_schedule = perform_parsing_today()
tomorrow_schedule = perform_parsing_tomorrow()
week_schedule = perform_parsing_week()

# Вставка данных в таблицу Schedule
cursor.execute('INSERT INTO schedule (today, tomorrow, week) VALUES (?, ?, ?)', (today_schedule, tomorrow_schedule, week_schedule))

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()
