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
    # Вычисляем завтрашнюю и послезавтрашнюю даты
    day1 = today + datetime.timedelta(days=1)
    day2 = today + datetime.timedelta(days=2)
    tomorrow_day = day1.weekday()
    after_tomorrow_day = day2.weekday()
    # Форматируем дату в формат (день.месяц.год)
    formatted_date_day1 = "{}.{}.{}".format(day1.day, day1.month, day1.year)
    formatted_date_day2 = "{}.{}.{}".format(day2.day, day2.month, day2.year)
    week_day1 = days_of_week[tomorrow_day]
    week_day2 = days_of_week[after_tomorrow_day]
    

    start_day = f'{week_day1} ({formatted_date_day1})'
    stop_day = f'{week_day2} ({formatted_date_day2})'
    print(start_day)
    print(stop_day)
    result = extract_text_between_words(schedule_text, start_day, stop_day)
    if result is not None:
        return result
    else:
        return "\nОшибка. Повторите попытку через пару минут. Если ошибка не исчезнет, обратитесь в тех. поддержку."
    

