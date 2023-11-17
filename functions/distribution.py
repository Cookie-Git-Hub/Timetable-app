from functions.db_extraction import extraction_db
import json

def get_user_data(user_id):
   with open('db\users.json', 'r') as json_file:
       data = json.load(json_file)
       users = data.get("users", [])
   for user in users:
       if user["id"] == user_id:
           return user
   return None, None, None  # Возвращаем None, если пользователь не найден

def user_data_variables(userid):
   user_id = userid
   user_data =  get_user_data(user_id)
   if user_data:
       faculty = user_data.get("faculty", "")
       course = user_data.get("course", "")
       group = user_data.get("group", "")
       result =  extraction_db(faculty, course, group)
       return result
   else:
       return "Вы не зарегистрированы. Пожалуйста, пройдите регистрацию."
