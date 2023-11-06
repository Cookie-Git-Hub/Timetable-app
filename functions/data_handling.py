import datetime
import re
from functions.distribution import user_data_variables


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


def perform_parsing_today(user_id):
    schedule_text = []
    schedule_text = user_data_variables(user_id)[0]

    def make_digits_bold(text):
        digits_bold = ''
        for char in text:
            if char.isdigit():
                digits_bold += f'<b>{char}</b>'
            else:
                digits_bold += char
        return digits_bold

    days_of_week = ["понедельник", "вторник", "среда",
                    "четверг", "пятница", "суббота", "воскресенье"]
    # Получаем текущую дату
    today = datetime.date.today()
    # Вычисляем завтрашнюю и послезавтрашнюю даты
    day1 = today
    day2 = today + datetime.timedelta(days=1)
    tomorrow_day = day1.weekday()
    after_tomorrow_day = day2.weekday()
    # Форматируем дату в формат (день.месяц.год)
    formatted_date_day1 = "{}.{}.{}".format(day1.day, day1.month, day1.year)
    formatted_date_day2 = "{}.{}.{}".format(day2.day, day2.month, day2.year)
    week_day1 = days_of_week[tomorrow_day]
    week_day2 = days_of_week[after_tomorrow_day]

    start_day = f'{week_day1} ({formatted_date_day1})'
    stop_day = f'{week_day2} ({formatted_date_day2})'
    result = extract_text_between_words(schedule_text, start_day, stop_day)
    if result is not None:
        text_with_bold_digits = make_digits_bold(result)
        return text_with_bold_digits
    else:
        start_word = 'Расписание занятий в БГЭУ'
        stop_word = 'Сервис носит оценочный характер, сверка с расписанием у Деканата ОБЯЗАТЕЛЬНА!'
        result2 = extract_text_between_words(
            schedule_text, start_word, stop_word)
        if result2 is not None:
            return '\nРасписание не найдено. Вероятно, сегодня выходной.'
        else:
            return "\nОшибка. Повторите попытку через пару минут. Если ошибка не исчезнет, обратитесь в тех. поддержку."


def perform_parsing_tomorrow(user_id):
    schedule_text = []
    schedule_text = user_data_variables(user_id)[0]
    def make_digits_bold(text):
        digits_bold = ''
        for char in text:
            if char.isdigit():
                digits_bold += f'<b>{char}</b>'
            else:
                digits_bold += char
        return digits_bold

    # Создаем список с названиями дней недели
    days_of_week = ["понедельник", "вторник", "среда",
                    "четверг", "пятница", "суббота", "воскресенье"]
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
    result = extract_text_between_words(schedule_text, start_day, stop_day)
    if result is not None:
        text_with_bold_digits = make_digits_bold(result)
        return text_with_bold_digits
    else:
        return "\nОшибка. Повторите попытку через пару минут. Если ошибка не исчезнет, обратитесь в тех. поддержку."


def perform_parsing_week(user_id):
    schedule_text = []
    schedule_text = user_data_variables(user_id)[0]
    print(schedule_text)
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
    result_parts = re.split(r'\n(?=\b[а-я]+\s\(\d+\.\d+\.\d+\))', result)
    for result_part in result_parts:
        result_list.append(result_part)
    result_text = '\n------------------------------------------------------------------------------\n'.join(
        result_list)
    text_with_bold_digits = make_digits_bold(result_text)
    return text_with_bold_digits
#    return "\nОшибка. Повторите попытку через пару минут. Если ошибка не исчезнет, обратитесь в тех. поддержку."
