
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def perform_parsing(faculty, course, group):
    options = wd.ChromeOptions()
    options.add_argument("--headless")
    driver = wd.Chrome(options=options)
    driver.get("http://bseu.by/schedule/")

    def parsing():
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

    parsing()

    schedule_elements = driver.find_element(By.ID, "content")
    schedule_text = schedule_elements.text

    driver.quit()
    return [schedule_text, faculty, course, group]