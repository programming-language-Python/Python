from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Котлетки"),
        ],
        [
            KeyboardButton(text="Макапошки"),
            KeyboardButton(text="Пюрешка")
        ],
    ],
    # * чтобы кнопки не занимали полэкрана
    resize_keyboard=True
)
