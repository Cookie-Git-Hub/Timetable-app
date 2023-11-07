import sqlite3

def extraction_db(faculty, course, group):
    normal_group = group.replace(" ", "_").replace("|", "_")
    # Создание или подключение к базе данных "schedule.db"
    connection = sqlite3.connect(
        f"db/course_{course}/{faculty}/{normal_group}.db")
    cursor = connection.cursor()

    # Запрос для извлечения расписания из таблицы "Schedule"
    cursor.execute('SELECT * FROM Schedule')
    data = cursor.fetchall()

    # Закрытие соединения с базой данных
    connection.close()

    if data:
        # Преобразование данных в текст
        text_data = "".join(" ".join(map(str, row)) for row in data)
        return text_data
    else:
        print("Произошла ошибка при извлечении данных из базы данных")
        return "Произошла ошибка при извлечении данных из базы данных"