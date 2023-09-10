# -*- coding: utf-8 -*-
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import re

def perform_parsing_week():

    driver = wd.Chrome()
    # Открываем страницу сайта
    driver.get("http://bseu.by/schedule/")

    def parsing_week():
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

    parsing_week()

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
    
    def make_digits_bold(text):
        digits_bold = ''
        for char in text:
            if char.isdigit():
                digits_bold += f'<b>{char}</b>'
            else:
                digits_bold += char
        return digits_bold
    
    result_list = []
    start_word = 'к./ауд.'
    stop_word = 'Сервис носит оценочный характер, сверка с расписанием у Деканата ОБЯЗАТЕЛЬНА!'
    result = extract_text_between_words(schedule_text, start_word, stop_word)
    if result is not None:
        result_parts = re.split(r'\n(?=\b[а-я]+\s\(\d+\.\d+\.\d+\))', result)
        for result_part in result_parts:
            result_list.append(result_part)
        result_text = '\n---------------------------------------------------------------------\n'.join(result_list)
        text_with_bold_digits = make_digits_bold(result_text)
        return text_with_bold_digits
    else:
        return "\nОшибка. Повторите попытку через пару минут. Если ошибка не исчезнет, обратитесь в тех. поддержку."
    

