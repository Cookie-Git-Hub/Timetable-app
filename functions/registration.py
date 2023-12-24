import json
from functions.parsing import perform_parsing_one
import os


def user_registration(user_id, faculty, course, group):
    # Проверяем, зарегистрирован ли пользователь
    with open('db/users.json', 'r') as json_file:
        data = json.load(json_file)

    users = data.get("users", [])

    for user in users:
        if user["id"] == user_id:
            return "Вы уже зарегистрированы! Если вы хотите изменить ваши данные, воспользуйтесь кнопкой 'Сменить данные ⚙️'."

    # Создаем нового пользователя и добавляем его в список
    new_user = {
        "id": user_id,
        "faculty": faculty,
        "course": course,
        "group": group,
        "blocked": False
    }

    users.append(new_user)

    # Сохраняем обновленные данные в JSON-файл
    data["users"] = users

    with open('db/users.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    normal_group = group.replace(" ", "_").replace("|", "_")
    db_path = f"db/course_{course}/{faculty}/{normal_group}.db"
    # Проверяем, существует ли файл базы данных
    if not os.path.isfile(db_path):
        # Файл не существует, вызываем соответствующую функцию или обработку ошибки
        perform_parsing_one(faculty, course, group)
        return "Вы были успешно зарегистрированы!"
    else:
        return "Вы были успешно зарегистрированы!"


def is_user_blocked(user_id):
    try:
        with open('db/users.json', 'r') as json_file:
            data = json.load(json_file)
            users = data.get("users", [])
    except FileNotFoundError:
        users = []

    for user in users:
        if user["id"] == user_id and user.get("blocked", False):
            return True

    return False


def remove_user(user_id):
    try:
        with open('db/users.json', 'r') as json_file:
            data = json.load(json_file)
            users = data.get("users", [])
    except FileNotFoundError:
        users = []

    updated_users = [user for user in users if user["id"] != user_id]

    with open('db/users.json', 'w') as json_file:
        json.dump({"users": updated_users}, json_file, indent=4)
    return True
