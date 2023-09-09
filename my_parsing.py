# -*- coding: utf-8 -*-
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import re

# def perform_timetable_parsing():

driver = wd.Chrome()
# Открываем страницу сайта
driver.get("http://bseu.by/schedule/")

def timetable_parsing():
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

    time.sleep(1)

    schedule_elements = driver.find_element(By.ID, "content")
    schedule_text = schedule_elements.text

    driver.quit()
    return schedule_text


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


text = timetable_parsing()
start_day = 'среда (13.9.2023)'
stop_day = 'четверг (14.9.2023)'
result = extract_text_between_words(text, start_day, stop_day)

if result is not None:
    print(result)
else:
    print("Стартовое и/или стоповое слово не найдены.")
