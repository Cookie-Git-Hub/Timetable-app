# -*- coding: utf-8 -*-
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import re

def perform_timetable_parsing():

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

    timetable_parsing()

    # Теперь вы можете извлечь информацию из расписания, например, с помощью XPath или CSS-селекторов
    schedule_elements = driver.find_element(By.ID, "content")
    schedule_text = schedule_elements.text

    driver.quit()
    return schedule_text

    # Добавьте функцию для извлечения расписания на конкретный день
def extract_schedule_for_day(schedule_text, day):
    # Используйте регулярное выражение для поиска точного совпадения даты
    pattern = re.compile(rf'{re.escape(day)}\s+\(\d+\.\d+\.\d+\)')
    matches = pattern.finditer(schedule_text)

    schedule_for_day = []
    found = False

    for match in matches:
        found = True
        start = match.start()
        end = schedule_text.find('\n', start)
        if end == -1:
            end = len(schedule_text)

        schedule_part = schedule_text[start:end]
        schedule_for_day.append(schedule_part)

    if not found:
        return f"Расписание на {day} не найдено в тексте:\n{schedule_text}"

    return '\n'.join(schedule_for_day)


# Пример использования:
day = "пятница (15.9.2023)"
schedule_text = perform_timetable_parsing()
schedule_for_day = extract_schedule_for_day(schedule_text, day)
print(schedule_for_day)
    
    
