import sqlite3
from functions.distribution import user_data_variables


# Получение данных для вставки
schedule = user_data_variables()[0]

# Создание или подключение к базе данных "schedule.db"
connection = sqlite3.connect(f"db/course_{course}/{faculty}/{group}.db")
cursor = connection.cursor()

# Создание таблицы Schedule, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS schedule (
    Schedule TEXT NOT NULL,
)
''')


# Вставка данных в таблицу Schedule
cursor.execute('INSERT INTO schedule (Schedule) VALUES (?)', (schedule))

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()
