from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

form_select = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дневная', callback_data='Дневная')],
    [InlineKeyboardButton(text='Заочная', callback_data='Заочная')]
])


course_select = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='1'),
    InlineKeyboardButton(text='2', callback_data='2')],
    [InlineKeyboardButton(text='3', callback_data='3'),
    InlineKeyboardButton(text='4', callback_data='4')]
])

main_kb = [
    [KeyboardButton(text="Сегодня 📖"),
    KeyboardButton(text="Завтра 📐")],
    [KeyboardButton(text="Неделя 📆"),
    KeyboardButton(text="Дополнительно ⚙️")]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите кнопку')

additional_menu_kb = [
    [KeyboardButton(text="Написать отзыв/жалобу 💌")],
    [KeyboardButton(text="Авторы 👑"),
    KeyboardButton(text="Назад 🔙")]
]

additional_menu = ReplyKeyboardMarkup(keyboard=additional_menu_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите кнопку')

feedback_menu_kb = [
    [KeyboardButton(text="Возврат в доп. меню 🔙")]
]

feedback_menu = ReplyKeyboardMarkup(keyboard=feedback_menu_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите кнопку')