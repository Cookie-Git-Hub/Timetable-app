from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import app.keyboards as kb
from db_extraction import print_today_schedule
from db_extraction import print_tomorrow_schedule
from db_extraction import print_week_schedule
from dotenv import load_dotenv
import os

load_dotenv()
router = Router()

bot = Bot(os.getenv('TOKEN'))

class FeedbackStates(StatesGroup):
    feedback_waiting = State()

# Хэндлер на команду /start
@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer("Привет! Это бот с учебных расписанием для БГЭУ.\nПока что расписание работает только для ДЦИ-1, 1 курс, 23 ДЦИ-1", reply_markup=kb.main)

@router.message(F.text.lower() == "сегодня 📖")
async def today(message: Message):
    text = print_today_schedule()
    await message.answer(f"<b>Раписание на сегодня:</b>{text}", parse_mode='HTML')

@router.message(F.text.lower() == "завтра 📐")
async def tomorrow(message: Message):
    text = print_tomorrow_schedule()
    await message.answer(f"<b>Раписание на завтра:</b>{text}", parse_mode='HTML')

@router.message(F.text.lower() == "неделя 📆")
async def week(message: Message):
    text = print_week_schedule()
    await message.answer(f"<b>Раписание на неделю:</b>{text}", parse_mode='HTML')

@router.message(F.text.lower() == "дополнительно ⚙️")
async def more(message: Message):
    await message.answer("Открываем доп. меню...", reply_markup=kb.additional_menu)

@router.message(F.text.lower() == "написать отзыв/жалобу 💌")
async def feedback(message: Message, state: FSMContext):
    await message.answer("Напишите Ваш отзыв/жалобу, мы их обязательно прочтём!", reply_markup=kb.feedback_menu)
    await state.set_state(FeedbackStates.feedback_waiting)

@router.message(FeedbackStates.feedback_waiting)
async def process_feedback(message: Message, state: FSMContext):
    await bot.forward_message(os.getenv('ID'), message.from_user.id, message.message_id)
    if message.text != "Возврат в доп. меню 🔙":    
        await message.answer("Сообщение отправлено разработчику. Спасибо!")
        await state.clear()
    else:
        async def go_back(message: Message):
            await message.answer("Возвращаемся...", reply_markup=kb.additional_menu)

@router.message(F.text.lower() == "возврат в доп. меню 🔙")
async def go_back(message: Message):
    await message.answer("Возвращаемся...", reply_markup=kb.additional_menu)

@router.message(F.text.lower() == "авторы 👑")
async def authors(message: Message):
    await message.answer("<b>Авторы этого замечательного бота:</b>\n@CookieRevolution и @ppestikk", parse_mode='HTML')

@router.message(F.text.lower() == "назад 🔙")
async def back(message: Message):
    await message.answer("Возвращаемся...", reply_markup=kb.main)

@router.message()
async def echo(message: Message):
    await message.answer('Я тебя не понимаю...')