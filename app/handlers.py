from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import app.keyboards as kb
from db_extraction import print_today_schedule
from db_extraction import print_tomorrow_schedule
from db_extraction import print_week_schedule
from functions.registration import user_registration, is_user_blocked, remove_user
from dotenv import load_dotenv
import os

load_dotenv()
router = Router()

bot = Bot(os.getenv('TOKEN'))


class FeedbackStates(StatesGroup):
    feedback_waiting = State()


class RegistrationStates(StatesGroup):
    faculty_waiting = State()
    course_waiting = State()
    group_waiting = State()


@router.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer("Привет! Я бот с учебным расписанием для БГЭУ.\nЯ показываю расписание почти для всех факультетов дневной формы обучения 👾")
    await message.answer("Чтобы я мог показать ваше расписание, пожалуйста, пройдите мини-регистрацию 📝", reply_markup=kb.registration)


@router.message(F.text.lower() == "регистрация 📝")
async def faculty(message: Message, state: FSMContext):
    await message.answer("Введите Ваш факультет:")
    await state.set_state(RegistrationStates.faculty_waiting)


@router.message(RegistrationStates.faculty_waiting)
async def course(message: Message, state: FSMContext):
    await message.answer("Введите курс:")
    global faculty
    faculty = message.text
    await state.set_state(RegistrationStates.course_waiting)


@router.message(RegistrationStates.course_waiting)
async def course(message: Message, state: FSMContext):
    await message.answer("Введите группу:")
    global course
    course = message.text
    await state.set_state(RegistrationStates.group_waiting)


@router.message(RegistrationStates.group_waiting)
async def success(message: Message, state: FSMContext):
    user_id = message.from_user.id
    group = message.text
    user_registration(user_id, faculty, course, group)
    await message.answer("Регистрация прошла успешно!")
    await message.answer("Приятного использования! Я буду очень рад, если, в случае неполадок, Вы сообщите мне об ошибке 🤖", reply_markup=kb.main)
    await state.clear()


@router.message(F.text.lower() == "сегодня 📖")
async def today(message: Message):
    user_id = message.from_user.id
    if is_user_blocked(user_id):
        await message.answer("Ты плохо себя вёл, так что я тебя заблокировал 🤡.")
    else:
        text = print_today_schedule()
        await message.answer(f"<b>Расписание на сегодня:</b>{text}", parse_mode='HTML')


@router.message(F.text.lower() == "завтра 📐")
async def tomorrow(message: Message):
    user_id = message.from_user.id
    if is_user_blocked(user_id):
        await message.answer("Ты плохо себя вёл, так что я тебя заблокировал 🤡.")
    else:
        text = print_tomorrow_schedule()
        await message.answer(f"<b>Расписание на завтра:</b>{text}", parse_mode='HTML')


@router.message(F.text.lower() == "неделя 📆")
async def week(message: Message):
    user_id = message.from_user.id
    if is_user_blocked(user_id):
        await message.answer("Ты плохо себя вёл, так что я тебя заблокировал 🤡.")
    else:
        text = print_week_schedule()
        await message.answer(f"<b>Расписание на неделю:</b>{text}", parse_mode='HTML')


@router.message(F.text.lower() == "дополнительно ⚙️")
async def more(message: Message):
    await message.answer("Открываем доп. меню...", reply_markup=kb.additional_menu)


@router.message(F.text.lower() == "написать отзыв 💌")
async def feedback(message: Message, state: FSMContext):
    await message.answer("Напишите Ваш отзыв, мы его обязательно прочтём!", reply_markup=kb.feedback_menu)
    await state.set_state(FeedbackStates.feedback_waiting)


@router.message(FeedbackStates.feedback_waiting)
async def process_feedback(message: Message, state: FSMContext):
    await bot.forward_message(os.getenv('ID'), message.from_user.id, message.message_id)
    if message.text != "Возврат в доп. меню 🔙":
        await message.answer("Сообщение отправлено разработчику. Спасибо!")
        await state.clear()
    else:
        await message.answer("Возвращаемся...", reply_markup=kb.additional_menu)


@router.message(F.text.lower() == "возврат в доп. меню 🔙")
async def go_back(message: Message):
    await message.answer("Возвращаемся...", reply_markup=kb.additional_menu)


@router.message(F.text.lower() == "авторы 👑")
async def authors(message: Message):
    await message.answer("<b>Авторы этого замечательного бота:</b>\n@CookieRevolution и @NAC_COOIlyaI", parse_mode='HTML')


@router.message(F.text.lower() == "сменить данные ⚙️")
async def change_data(message: Message):
    user_id = message.from_user.id
    remove_user(user_id)
    await message.answer("Ваш профиль был удалён. Пройдите регистрацию заново 📝", reply_markup=kb.registration)


@router.message(F.text.lower() == "назад 🔙")
async def back(message: Message):
    await message.answer("Возвращаемся...", reply_markup=kb.main)

    
@router.message()
async def echo(message: Message):
    await message.answer('Я тебя не понимаю...')
