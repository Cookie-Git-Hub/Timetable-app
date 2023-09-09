# -*- coding: utf-8 -*-
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import datetime

def perform_parsing_tomorrow():

    driver = wd.Chrome()
    # Открываем страницу сайта
    driver.get("http://bseu.by/schedule/")

    def parsing_tomorrow():
        faculty_select = Select(driver.find_element(By.ID, "faculty"))
        faculty_select.select_by_visible_text("ФЦЭ")
        time.sleep(0.2)

        form_select = Select(driver.find_element(By.ID, "form"))
        form_select.select_by_visible_text("Дневная")
        time.sleep(0.2)

        course_select = Select(driver.find_element(By.ID, "course"))
        course_select.select_by_visible_text("1")
        time.sleep(0.2)

        group_select = Select(driver.find_element(By.ID, "group"))
        group_select.select_by_visible_text("23 ДЦИ-1 | Экономическая информатика")
        time.sleep(0.2)

        select_period = driver.find_element(By.ID, "pweek")
        select_period.click()
        time.sleep(0.2)

        btn_click = driver.find_element(By.ID, "btn")
        btn_click.click()

        time.sleep(0.3)

    parsing_tomorrow()

    schedule_elements = driver.find_element(By.ID, "content")
    schedule_text = schedule_elements.text

    driver.quit()

    def extract_text_between_words(input_text, start_word, stop_word):
        # Ищем индекс начала и конца искомого текста
        start_index = input_text.find(start_word)
        stop_index = input_text.find(stop_word)

        # Проверяем, что стартовое и стоповое слова найдены
        if start_index == -1 or stop_index == -1:
            return None  # Возвращаем None, если слова не найдены

        # Извлекаем текст между стартовым и стоповым словами
        extracted_text = input_text[start_index + len(start_word):stop_index]

        return extracted_text
    
    # Создаем список с названиями дней недели
    days_of_week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    # Получаем текущую дату
    today = datetime.date.today()
    today_day = today.weekday()
    # Вычисляем завтрашнюю дату
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow_day = tomorrow.weekday()
    # Форматируем дату в формат (день.месяц.год)
    formatted_date_today = today.strftime("%d.%m.%Y")
    formatted_date_tomorrow = tomorrow.strftime("%d.%m.%Y")
    week_today = days_of_week[today_day]
    week_tomorrow = days_of_week[tomorrow_day]

    start_day = f'{week_today} ({formatted_date_today})'
    stop_day = f'{week_tomorrow} ({formatted_date_tomorrow})'
    print(start_day)
    print(stop_day)
    result = extract_text_between_words(schedule_text, start_day, stop_day)
    if result is not None:
        return result
    else:
        return "Ошибка. Повторите попытку через пару минут. Если ошибка не исчезнет, обратитесь в тех. поддержку."
    

