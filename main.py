import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from functions.today import parsing_today


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
            types.KeyboardButton(text="Опции")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите кнопку :)"
    )
    await message.answer("Привет! Это бот с учебных расписанием для БГЭУ.\nПока что расписание работает только для ФЦЭ, 1 курс, 23 ДЦИ-1", reply_markup=keyboard)

@dp.message(F.text.lower() == "сегодня")
async def with_puree(message: types.Message):
    text = parsing_today()
    await message.reply(text)

@dp.message(F.text.lower() == "завтра")
async def without_puree(message: types.Message):
    text = parsing_tomorrow()
    await message.reply(text)

@dp.message(F.text.lower() == "неделя")
async def with_puree(message: types.Message):
    text = parsing_week()
    await message.reply(text)

@dp.message(F.text.lower() == "опции")
async def without_puree(message: types.Message):
    text = options()
    await message.reply(text)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())