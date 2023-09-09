from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs
import time

url = "http://bseu.by/schedule/"

def perform_timetable_parsing_week():

    driver = wd.Chrome()
    # Открываем страницу сайта
    driver.get(url)

    def timetable_parsing_tomorrow():
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

        select_period = driver.find_element(By.ID, "pday")
        select_period.click()
        time.sleep(0.2)

        btn_click = driver.find_element(By.ID, "btn")
        btn_click.click()

        time.sleep(0.5)

        page_source = driver.page_source
        soup = bs(page_source, 'html.parser')
        select_period = soup.find_element(By.ID, "pday")

        table = soup.find('table', class_='schedule-table')

        return f'Расписание на сегодня:/n'































    timetable_parsing_tomorrow()

    # Теперь вы можете извлечь информацию из расписания, например, с помощью XPath или CSS-селекторов
    schedule_elements = driver.find_elements(By.XPATH, "//div[@id='content']")
    schedule_text = "\n".join([element.text for element in schedule_elements])

    driver.quit()
    return schedule_text

    
    
    
