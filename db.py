import sqlite3

def fill_db(schedule):
    # Получение данных для вставки
    schedule_text = schedule[0]
    faculty = schedule[1]
    course = schedule[2]
    group = schedule[3]

    print(schedule_text)

    # Создание или подключение к базе данных "schedule.db"
    connection = sqlite3.connect("db/course_1/ФЦЭ/23_ДЦИ-1.db")
    cursor = connection.cursor()

    # Создание таблицы Schedule, если она не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS schedule (
        Schedule TEXT NOT NULL
    )
    ''')

    # Вставка данных в таблицу Schedule
    for text in schedule_text:
        cursor.execute('INSERT INTO schedule (Schedule) VALUES (?)', (text,))


    # Сохранение изменений и закрытие соединения
    connection.commit()
    connection.close()
    return True
