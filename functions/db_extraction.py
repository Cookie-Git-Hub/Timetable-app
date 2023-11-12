import sqlite3
import os


async def extraction_db(faculty, course, group):
    normal_group = group.replace(" ", "_").replace("|", "_")
    db_path = f"db/course_{course}/{faculty}/{normal_group}.db"
    # Проверяем, существует ли файл базы данных
    if not os.path.isfile(db_path):
        # Файл не существует, вызываем соответствующую функцию или обработку ошибки
        return "Файл не существует, ошибка"

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
        return "Произошла ошибка при извлечении данных из базы данных"
