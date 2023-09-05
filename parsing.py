from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = wd.Chrome()
# Открываем страницу сайта
driver.get("http://bseu.by/schedule/")

def timetable_parsing():
    faculty_select = Select(driver.find_element(By.ID, "faculty"))
    faculty_select.select_by_visible_text("ФЦЭ")
    time.sleep(0.02)

    form_select = Select(driver.find_element(By.ID, "form"))
    form_select.select_by_visible_text("Дневная")
    time.sleep(0.02)

    course_select = Select(driver.find_element(By.ID, "course"))
    course_select.select_by_visible_text("1")
    time.sleep(0.02)

    group_select = Select(driver.find_element(By.ID, "group"))
    group_select.select_by_visible_text("23 ДЦИ-1 | Экономическая информатика")
    time.sleep(0.02)

    select_period = driver.find_element(By.ID, "pweek")
    select_period.click()
    time.sleep(0.02)

    btn_click = driver.find_element(By.ID, "btn")
    btn_click.click()

    time.sleep(0.1)

    # Теперь вы можете извлечь информацию из расписания, например, с помощью XPath или CSS-селекторов
    schedule_elements = driver.find_elements(By.XPATH, "//div[@id='content']")
    for schedule_element in schedule_elements:
        print(schedule_element.text)

    driver.quit()
    return schedule_elements
