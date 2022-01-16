
# * запуск бота
import asyncio

# * Dispatcher - доставщик update
# * executer - начинает работу бота. Запускает бота
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

# * поток в котором обрабатываются все события
loop = asyncio.get_event_loop()
# * parse_mode - для форматирования
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

# * если запущен этот файл и он не импортирован
if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
