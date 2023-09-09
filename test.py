import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from functions.today import perform_parsing_today
from functions.tomorrow import perform_parsing_tomorrow
from functions.week import perform_parsing_week

developer_telegram_id = 851099138

feedback_button = types.InlineKeyboardButton(text="Написать отзыв/жалобу", callback_data="feedback")
# feedback_keyboard = types.InlineKeyboardMarkup().add(feedback_button)

#Получаем токен из защищённого файла
with open('config.env', 'r') as file:
    token = file.readline()
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Сегодня"),
            types.KeyboardButton(text="Завтра"),
            types.KeyboardButton(text="Неделя"),
            types.KeyboardButton(text="Дополнительно")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите кнопку :)"
    )
    await message.answer("Привет! Это бот с учебных расписанием для БГЭУ.\nПока что расписание работает только для ФЦЭ, 1 курс, 23 ДЦИ-1", reply_markup=keyboard)

@dp.message(F.text.lower() == "сегодня")
async def today(message: types.Message):
    text = perform_parsing_today()
    await message.reply(f"<b>Раписание на сегодня:</b>{text}", parse_mode='HTML')

@dp.message(F.text.lower() == "завтра")
async def tomorrow(message: types.Message):
    text = perform_parsing_tomorrow()
    await message.reply(f"<b>Раписание на завтра:</b>{text}", parse_mode='HTML')

@dp.message(F.text.lower() == "неделя")
async def week(message: types.Message):
    text = perform_parsing_week()
    await message.reply(f"<b>Раписание на неделю:</b>{text}", parse_mode='HTML')

@dp.message(F.text.lower() == "дополнительно")
async def more(message: types.Message):
    await message.reply("Доп. меню:", reply_markup=feedback_keyboard)

@dp.message(F.text.lower() == "написать отзыв/жалобу")
async def feedback(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Возврат в доп. меню")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Напишите Ваш отзыв/жалобу, мы их обязательно прочтём!"
    )
    await message.reply(" ", reply_markup=keyboard)
    await bot.forward_message(chat_id=developer_telegram_id, from_chat_id=message.chat.id, message_id=message.message_id)
    await message.reply("Сообщение отправлено разработчику. Спасибо!")

@dp.message(F.text.lower() == "возврат в доп. меню")
async def go_back(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Написать отзыв/жалобу"),
            types.KeyboardButton(text="Авторы"),
            types.KeyboardButton(text="Назад")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите кнопку :)"
    )
    await message.reply("Возврат в доп. меню:", reply_markup=keyboard)

@dp.message(F.text.lower() == "авторы")
async def authors(message: types.Message):
    await message.reply("<b>Авторы этого замечательного бота:</b>\n@CookieRevolution и @ppestikk", parse_mode='HTML')

@dp.message(F.text.lower() == "назад")
async def back(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Сегодня"),
            types.KeyboardButton(text="Завтра"),
            types.KeyboardButton(text="Неделя"),
            types.KeyboardButton(text="Дополнительно")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите кнопку :)"
    )
    await message.answer("Возврат в главное меню.", reply_markup=keyboard)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())