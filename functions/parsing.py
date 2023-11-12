from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import json
import sqlite3
import threading


async def fill_db(schedule_text, faculty, course, group):
    print("fill_db" + course + "/" + faculty + "/" + group)

    normal_group = group.replace(" ", "_").replace("|", "_")

    # Создание или подключение к базе данных "schedule.db"
    connection = sqlite3.connect(
        f"db/course_{course}/{faculty}/{normal_group}.db")
    cursor = connection.cursor()

    # Создание таблицы Schedule, если она не существует
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Schedule (
        Schedule TEXT NOT NULL
    )
    ''')

    # Вставка данных в таблицу Schedule
    for text in schedule_text:
        cursor.execute('INSERT INTO Schedule (Schedule) VALUES (?)', (text,))

    # Сохранение изменений и закрытие соединения
    connection.commit()
    connection.close()
    return True



async def perform_parsing_one(faculty, course, group):
    options = wd.ChromeOptions()
    options.add_argument("--headless")
    driver = wd.Chrome(options=options)
    driver.get("http://bseu.by/schedule/")

    async def parsing():
        faculty_select = Select(driver.find_element(By.ID, "faculty"))
        faculty_select.select_by_visible_text(f"{faculty}")
        time.sleep(0.2)

        form_select = Select(driver.find_element(By.ID, "form"))
        form_select.select_by_visible_text("Дневная")
        time.sleep(0.2)

        course_select = Select(driver.find_element(By.ID, "course"))
        course_select.select_by_visible_text(f"{course}")
        time.sleep(0.2)

        group_select = Select(driver.find_element(By.ID, "group"))
        group_select.select_by_visible_text(f"{group}")
        time.sleep(0.2)

        select_period = driver.find_element(By.ID, "pweek")
        select_period.click()
        time.sleep(0.2)

        btn_click = driver.find_element(By.ID, "btn")
        btn_click.click()

        time.sleep(0.2)

    await parsing()

    schedule_elements = driver.find_element(By.ID, "content")
    schedule_text = schedule_elements.text
    print("schedule_text" + schedule_text + "schedule_text")
    driver.quit()

    await fill_db(schedule_text, faculty, course, group)


async def perform_parsing():
    with open('db/users.json', 'r') as json_file:
        data = json.load(json_file)
        users = data.get("users", [])

    for user in users:
        faculty = user.get("faculty", "")
        course = user.get("course", "")
        group = user.get("group", "")
        # await test(faculty, course, group)
        parsing_thread = threading.Thread(target=perform_parsing_one, args=(faculty, course, group))
        parsing_thread.start()


