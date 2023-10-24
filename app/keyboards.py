from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton)

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