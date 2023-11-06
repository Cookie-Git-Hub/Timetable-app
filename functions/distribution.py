from parsing import perform_parsing
import json
    
text = perform_parsing()
def get_user_data(user_id):
    with open('db/users.json', 'r') as json_file:
        data = json.load(json_file)
        users = data.get("users", [])

    for user in users:
        if user["id"] == user_id:
            return user.get("faculty"), user.get("course"), user.get("group")

    return None, None, None  # Возвращаем None, если пользователь не найден


def user_data_variables(userid):
    user_id = userid
    user_data = get_user_data(user_id)

    if user_data:
        faculty = user_data.get("faculty", "")
        course = user_data.get("course", "")
        group = user_data.get("group", "")
        
        schedule_text = perform_parsing(faculty, course, group)
        return schedule_text
    else:
        return "Вы не зарегистрированы. Пожалуйста, пройдите регистрацию."