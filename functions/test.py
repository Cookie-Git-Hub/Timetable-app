import datetime
import pytz

# Получаем текущую дату
moscow_tz = pytz.timezone('Europe/Moscow')
moscow_time = datetime.datetime.now(moscow_tz)
print (today = moscow_time.date())
# today = datetime.date.today()

# Вычисляем завтрашнюю и послезавтрашнюю даты
# day1 = today
# day2 = today + datetime.timedelta(days=1)
# tomorrow_day = day1.weekday()
# after_tomorrow_day = day2.weekday()