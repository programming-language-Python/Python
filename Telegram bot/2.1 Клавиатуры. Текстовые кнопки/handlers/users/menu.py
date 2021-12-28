from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu


@dp.message_handler(Command("menu"))
# * message: тип
async def show_menu(message: Message):
    await message.answer("Выберите товар из меню ниже", reply_markup=menu)

# * Ловим все три кнопки

# * если выбрали что-то из этого списка


@dp.message_handler(Text(equals=["Котлетки", "Макарошки", "Пюрешка"]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо",
                         reply_markup=ReplyKeybordRemove())
# * Вариант 2 - @dp.message_handler(text="Пюрешка")
# * Вариант 3 - @dp.message_handler(Text(equals="Пюрешка"))
