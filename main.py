import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from dotenv import load_dotenv
import os
#Импорт функций
import keyboards as kb
from functions.today import perform_parsing_today
from functions.tomorrow import perform_parsing_tomorrow
from functions.week import perform_parsing_week


load_dotenv()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(os.getenv('TOKEN'))
# Диспетчер
dp = Dispatcher(bot=bot)

# Хэндлер на команду /start
@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer("Привет! Это бот с учебных расписанием для БГЭУ.\nПока что расписание работает только для ФЦЭ, 1 курс, 23 ДЦИ-1", reply_markup=kb.main)

@dp.message(F.button == "сегодня")
async def today(message: Message):
    text = perform_parsing_today()
    await message.answer(f"<b>Раписание на сегодня:</b>{text}", parse_mode='HTML')

@dp.message(F.text.lower() == "завтра")
async def tomorrow(message: Message):
    text = perform_parsing_tomorrow()
    await message.answer(f"<b>Раписание на завтра:</b>{text}", parse_mode='HTML')

@dp.message(F.text.lower() == "неделя")
async def week(message: Message):
    text = perform_parsing_week()
    await message.answer(f"<b>Раписание на неделю:</b>{text}", parse_mode='HTML')

@dp.message(F.text.lower() == "дополнительно")
async def more(message: Message):
    await message.answer("Открываем доп. меню...:", reply_markup=kb.additional_menu)

@dp.message(lambda message: message.text == "Написать отзыв/жалобу")
async def feedback(message: Message):
    await message.answer("Напишите Ваш отзыв/жалобу, мы их обязательно прочтём!", reply_markup=kb.feedback_menu)
    await bot.forward_message(os.getenv('ID'), from_chat_id=message.chat.id, message_id=message.message_id)
    await message.answer("Сообщение отправлено разработчику. Спасибо!")

@dp.message(F.text.lower() == "возврат в доп. меню")
async def go_back(message: Message):
    await message.answer("Возвращаемся...", reply_markup=kb.additional_menu)

@dp.message(F.text.lower() == "авторы")
async def authors(message: Message):
    await message.answer("<b>Авторы этого замечательного бота:</b>\n@CookieRevolution и @ppestikk", parse_mode='HTML')

@dp.message(F.text.lower() == "назад")
async def back(message: Message):
    await message.answer("Возвращаемся...", reply_markup=kb.main)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())