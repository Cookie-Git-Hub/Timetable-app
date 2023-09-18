from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def perform_parsing_today():

    # driver = wd.Chrome()
    # # Открываем страницу сайта
    # driver.get("http://bseu.by/schedule/")

    options = wd.ChromeOptions()
    options.add_argument("--headless")
    driver = wd.Chrome(options=options)
    driver.get("http://bseu.by/schedule/")


    def parsing_today():
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

        time.sleep(0.3)

    parsing_today()

    # Теперь вы можете извлечь информацию из расписания, например, с помощью XPath или CSS-селекторов
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
    
    start_word = 'к./ауд.'
    stop_word = 'Сервис носит оценочный характер, сверка с расписанием у Деканата ОБЯЗАТЕЛЬНА!'
    result = extract_text_between_words(schedule_text, start_word, stop_word)
    if result is not None:
        text_with_bold_digits = make_digits_bold(result)
        return text_with_bold_digits
    else:
        start_word = 'Расписание занятий в БГЭУ'
        stop_word = 'Сервис носит оценочный характер, сверка с расписанием у Деканата ОБЯЗАТЕЛЬНА!'
        result2 = extract_text_between_words(schedule_text, start_word, stop_word)
        if result2 is not None:
            return '\nРасписание не найдено. Вероятно, сегодня выходной.'
        else:
            return "\nОшибка. Повторите попытку через пару минут. Если ошибка не исчезнет, обратитесь в тех. поддержку."
    
    
