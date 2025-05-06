import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logger.add("bot.log", rotation="10 MB", level="INFO")

# Инициализация бота и диспетчера
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    logger.error("Токен бота не найден. Проверьте файл .env")
    exit(1)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчики команд
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Я ваш бот-ассистент."
    )
    logger.info(f"Пользователь {message.from_user.id} запустил бота")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    help_text = """
    Доступные команды:
    /start - Начать взаимодействие с ботом
    /help - Показать список команд
    """
    await message.answer(help_text)

# Обработчик текстовых сообщений
@dp.message()
async def echo_message(message: Message):
    await message.answer(f"Вы написали: {message.text}")
    logger.info(f"Пользователь {message.from_user.id} отправил сообщение: {message.text}")

# Запуск бота
async def main():
    logger.info("Бот запущен")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main()) 