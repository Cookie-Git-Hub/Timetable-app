import json

def decode():
    # Открываем JSON-файл с указанием кодировки utf-8
    with open('db/users.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Перебираем пользователей и декодируем escape-последовательности Unicode
    for user in data['users']:
        user['faculty'] = user['faculty'].encode('utf-8').decode('unicode-escape')
        user['group'] = user['group'].encode('utf-8').decode('unicode-escape')

    # Перезаписываем JSON-файл с обновленными данными     
    with open('db/users.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
























