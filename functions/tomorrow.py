from selenium import webdriver as wd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time

url = "http://bseu.by/schedule/"

def perform_timetable_parsing_tomorrow():

    driver = wd.Chrome()
    # Открываем страницу сайта
    driver.get(url)
    wait = WebDriverWait(driver, 0.5)

    def timetable_parsing_tomorrow():
        faculty_select = wait.until(EC.presence_of_element_located((By.ID, "faculty")))
        faculty_select.select_by_visible_text("ФЦЭ")
        

        form_select = wait.until(EC.presence_of_element_located((By.ID, "form")))
        form_select.select_by_visible_text("Дневная")

        course_select = wait.until(EC.presence_of_element_located((By.ID, "course")))
        course_select.select_by_visible_text("1")

        group_select = wait.until(EC.presence_of_element_located((By.ID, "group")))
        group_select.select_by_visible_text("23 ДЦИ-1 | Экономическая информатика")

        select_period = driver.find_element(By.ID, "pweek")
        select_period.click()

        btn_click = driver.find_element(By.ID, "btn")
        btn_click.click()

        time.sleep(0.5)

        page_source = driver.page_source
        soup = bs(page_source, 'html.parser')
        table = soup.find('table', class_='sched')

        


    timetable_parsing_tomorrow()

    driver.quit()
    return ret
    

        


    # # Теперь вы можете извлечь информацию из расписания, например, с помощью XPath или CSS-селекторов
    # schedule_elements = driver.find_elements(By.XPATH, "//div[@id='content']")
    # schedule_text = "\n".join([element.text for element in schedule_elements])































    timetable_parsing_tomorrow()

    # Теперь вы можете извлечь информацию из расписания, например, с помощью XPath или CSS-селекторов
    schedule_elements = driver.find_elements(By.XPATH, "//div[@id='content']")
    schedule_text = "\n".join([element.text for element in schedule_elements])

    driver.quit()
    return schedule_text

    
    
    
