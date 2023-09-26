from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
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

faculty_list = [
    "Аспир.", "ВШУБ", "ИСГО", "Магистр.", "УЭФ", "ФКТИ", "ФМБК", "ФМк", "ФМЭО", "ФП", "ФФБД", "ФЦЭ", "ФЭМ"
]

group_list = [
    
]

# Хэндлер на команду /start
@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer("Привет! Чтобы я знал какое расписание тебе показывать, сначала придётся пройти мини-регистрацию. Напиши название своего факультета ниже 👾\nПример: ФЦЭ ✅", reply_markup=kb.main)

@router.message()
async def faclty(message: Message):
    if message.text in faculty_list:
        global faculty
        faculty = message.text
        await message.answer('Выберите форму обучения', reply_markup=kb.form_select)
    else:
        await message.answer('Ошибка🤕\nВозможные проблемы:\n1. Неправильно указан факультет(проверьте, совпадает ли написанный вами факультет с тем, как он написан на сайте университета с расписанием).\n2. Этот факультет не обслуживается, чтобы увидеть список обсуживаемых факультетов, напишите "/list".\n3. Возможна ошибка в работе бота, просьба повторить попытку через несколько минут.')
    
@router.callback_query(F.data == 'Дневная')
async def day_form(callback: CallbackQuery):
    global stationarity
    stationarity = callback.data
    await callback.message.answer(f'Выбранная форма обучения: <b>{callback.data}</b>', parse_mode='HTML')
    await callback.message.answer('Выберите курс', reply_markup = kb.course_select)

@router.callback_query(F.data == 'Заочная')
async def day_form(callback: CallbackQuery):
    global stationarity
    stationarity = callback.data
    await callback.message.answer(f'Выбранная форма обучения: <b>{callback.data}</b>', parse_mode='HTML')
    await callback.message.answer('Выберите курс', reply_markup = kb.course_select)

@router.callback_query(F.data == '1')
async def day_form(callback: CallbackQuery):
    global course
    course = callback.data
    await callback.message.answer(f'Выбранный курс: <b>{callback.data}</b>', parse_mode='HTML')
    await callback.message.answer('Напишите название вашей группы\nПример: 23 ДЦИ-1 ✅')

@router.callback_query(F.data == '2')
async def day_form(callback: CallbackQuery):
    global course
    course = callback.data
    await callback.message.answer(f'Выбранный курс: <b>{callback.data}</b>', parse_mode='HTML')
    await callback.message.answer('Напишите название вашей группы\nПример: 23 ДЦИ-1 ✅')

@router.callback_query(F.data == '3')
async def day_form(callback: CallbackQuery):
    global course
    course = callback.data
    await callback.message.answer(f'Выбранная форма обучения: <b>{callback.data}</b>', parse_mode='HTML')
    await callback.message.answer('Напишите название вашей группы\nПример: 23 ДЦИ-1 ✅')

@router.callback_query(F.data == '4')
async def day_form(callback: CallbackQuery):
    global course
    course = callback.data
    await callback.message.answer(f'Выбранная форма обучения: <b>{callback.data}</b>', parse_mode='HTML')
    await callback.message.answer('Напишите название вашей группы\nПример: 23 ДЦИ-1 ✅')

@router.message()
async def faclty(message: Message):
    if message.text in group_list:
            global group
            group = message.text
            await message.answer(f'Выбранная группа: <b>{group}</b>', parse_mode='HTML')
            await message.answer('<b>Регистрация закончена!\nБлагодарю за ожидание, теперь вы можете перейти к использованию бота. Если возникнут какие-то проблемы, не стесняйтесь пользоваться обратной связью</b> 💌', parse_mode='HTML')
    else:
        await message.answer('Ошибка🤕\nВозможные проблемы:\n1. Неправильно указана группа(проверьте, совпадает ли написанная вами группа с тем, как она написана на сайте университета с расписанием).\n2. Возможна ошибка в работе бота, просьба повторить попытку через несколько минут.')

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