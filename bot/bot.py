import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from loguru import logger

from music_service import MusicService
from keyboards import get_main_keyboard, get_search_results_keyboard, get_track_inline_keyboard

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logger.add("bot.log", rotation="10 MB", level="INFO")

# Инициализация бота и диспетчера
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    logger.error("Токен бота не найден. Проверьте файл .env")
    exit(1)

# Название бота (будет добавляться к названию песни)
BOT_NAME = "@hxmusic_robot"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Инициализация сервиса поиска музыки
try:
    music_service = MusicService()
except Exception as e:
    logger.error(f"Не удалось инициализировать сервис поиска музыки: {e}")
    music_service = None

# Глобальное хранилище результатов поиска 
search_results = {}
# Хранилище для сообщений с результатами поиска
search_messages = {}

# Обработчики команд
@dp.message(Command("start"))
async def cmd_start(message: Message):
    start_text = f"""
<b>🎵 Привет, {message.from_user.first_name}! 🎵</b>

Я твой личный <b>музыкальный ассистент</b>. Буду помогать тебе находить любимую музыку в считанные секунды!

<b>🔍 Как пользоваться:</b>
• Просто напиши название песни или исполнителя
• Выбери трек из списка
• Получи полную версию песни прямо в чате

<b>⚡️ Быстро и легко, без ссылок и рекламы!</b>
"""
    await message.answer(
        start_text,
        parse_mode="HTML",
        reply_markup=get_main_keyboard()
    )
    logger.info(f"Пользователь {message.from_user.id} запустил бота")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    help_text = """
<b>📚 ПОМОЩЬ И КОМАНДЫ 📚</b>

<b>🎯 Основные команды:</b>
• /start - Перезапуск бота
• /help - Это меню помощи

<b>🎧 Как найти музыку:</b>
1. Напиши <i>название песни</i> или <i>имя исполнителя</i>
2. Выбери подходящий трек из списка
3. Дождись загрузки и наслаждайся музыкой!

<b>💡 Советы:</b>
• Для точного поиска указывай и исполнителя, и название трека
• Можно искать на русском или английском языке
• Чем конкретнее запрос, тем точнее результат

<b>🔊 Качество:</b> Все треки загружаются в максимально доступном качестве.

<b>🌐 Источники:</b> Поиск осуществляется через Spotify API.

<b>💬 Поддержка:</b> Если у тебя возникли трудности или вопросы, пиши в поддержку: @crypthx
"""
    await message.answer(help_text, parse_mode="HTML", reply_markup=get_main_keyboard())

# Обработчики текстовых команд из клавиатуры
@dp.message(F.text == "ℹ️ Помощь")
async def text_help(message: Message):
    await cmd_help(message)

@dp.message(F.text == "👋 О боте")
async def text_about(message: Message):
    about_text = """
<b>🎧 HX Music Bot 🎧</b>

<b>🚀 Возможности:</b>
• Мгновенный поиск миллионов треков
• Скачивание полных версий песен

<b>📈 Преимущества:</b>
• Быстрый поиск и скачивание
• Интуитивно понятный интерфейс
• Никакой рекламы и отвлекающих факторов
• Регулярные обновления и улучшения

<b>🔍 Начни поиск прямо сейчас!</b>
Просто напиши название любимой песни.
"""
    await message.answer(about_text, parse_mode="HTML", reply_markup=get_main_keyboard())

# Обработчики инлайн-кнопок
@dp.callback_query(F.data.startswith("track:"))
async def process_track_selection(callback: CallbackQuery):
    user_id = callback.from_user.id
    track_idx = int(callback.data.split(":")[1])
    
    if user_id not in search_results or not search_results[user_id]:
        await callback.answer("Результаты поиска устарели. Пожалуйста, выполните новый поиск.", show_alert=True)
        return
    
    if track_idx >= len(search_results[user_id]):
        await callback.answer("Трек не найден. Пожалуйста, попробуйте снова.", show_alert=True)
        return
    
    track = search_results[user_id][track_idx]
    
    # Информируем пользователя о начале загрузки
    await callback.answer("Загружаю песню, пожалуйста, подождите...")
    
    # Отправляем сообщение о начале загрузки
    status_msg = await callback.message.answer(
        f"<b>⏳ Загружаю трек:</b>\n🎵 <b>{track['name']}</b>\n🎤 <b>{track['artist']}</b>\n\nПожалуйста, подождите, это может занять некоторое время...",
        parse_mode="HTML"
    )
    
    # Показываем индикатор загрузки файла
    await bot.send_chat_action(chat_id=callback.message.chat.id, action="upload_document")
    
    try:
        # Загружаем песню
        file_path = await music_service.download_full_song(track)
        
        if file_path and os.path.exists(file_path):
            # Отправляем только аудиофайл без дополнительной информации
            audio_file = FSInputFile(file_path)
            await callback.message.answer_audio(
                audio=audio_file,
                performer=track['artist'],
                title=f"{track['name']} | {BOT_NAME}",
                caption=f"🎵 <b>{track['name']}</b> - {track['artist']} | {BOT_NAME}",
                parse_mode="HTML"
            )
            
            # Удаляем сообщение о загрузке
            await status_msg.delete()
            
            # Удаляем сообщение с результатами поиска
            if user_id in search_messages and search_messages[user_id]:
                try:
                    await callback.message.delete()
                    search_messages[user_id] = None
                except Exception as e:
                    logger.error(f"Ошибка при удалении сообщения с результатами поиска: {e}")
        else:
            # Если загрузка не удалась, показываем сообщение об ошибке
            await status_msg.edit_text(
                f"❌ <b>Не удалось загрузить трек</b>\n\n🎵 <b>{track['name']}</b>\n🎤 <b>{track['artist']}</b>\n\nПожалуйста, попробуйте другой трек или повторите попытку позже.",
                parse_mode="HTML"
            )
    except Exception as e:
        logger.error(f"Ошибка при загрузке/отправке аудиофайла: {e}")
        await status_msg.edit_text(
            f"❌ <b>Произошла ошибка при обработке трека</b>\n\n🎵 <b>{track['name']}</b>\n🎤 <b>{track['artist']}</b>\n\nПожалуйста, попробуйте другой трек.",
            parse_mode="HTML"
        )

@dp.callback_query(F.data.startswith("page:"))
async def process_pagination(callback: CallbackQuery):
    user_id = callback.from_user.id
    page = int(callback.data.split(":")[1])
    
    if user_id not in search_results or not search_results[user_id]:
        await callback.answer("Результаты поиска устарели. Пожалуйста, выполните новый поиск.", show_alert=True)
        return
    
    tracks = search_results[user_id]
    keyboard = get_search_results_keyboard(tracks, page)
    
    await callback.message.edit_text(
        f"<b>🎵 Найдено {len(tracks)} треков</b>\n\nВыберите трек для скачивания 👇",
        parse_mode="HTML",
        reply_markup=keyboard
    )
    
    await callback.answer()

@dp.callback_query(F.data == "new_search")
async def process_new_search(callback: CallbackQuery):
    await callback.message.answer(
        "Введите название песни или имя исполнителя для поиска:",
        reply_markup=get_main_keyboard()  # Сохраняем клавиатуру
    )
    await callback.answer()

# Общий обработчик для всех текстовых сообщений
@dp.message(~F.text.startswith('/'))
async def echo_message(message: Message):
    # Любое сообщение пользователя запускает поиск
    await perform_search(message, message.text)

# Вспомогательные функции
async def perform_search(message: Message, query: str):
    if not music_service:
        await message.answer(
            "❌ <b>К сожалению, сервис поиска музыки сейчас недоступен.</b>\nПожалуйста, попробуйте позже.",
            parse_mode="HTML",
            reply_markup=get_main_keyboard()
        )
        return
    
    # Показываем индикатор набора текста
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    # Выполняем поиск
    tracks = await music_service.search_track(query, limit=15)
    
    # Сохраняем результаты для конкретного пользователя
    user_id = message.from_user.id
    search_results[user_id] = tracks
    
    if not tracks:
        await message.answer(
            f"❌ <b>По запросу '{query}' ничего не найдено.</b>\n\nПопробуйте изменить запрос или написать на английском языке.",
            parse_mode="HTML",
            reply_markup=get_main_keyboard()
        )
        return
    
    # Отображаем результаты
    keyboard = get_search_results_keyboard(tracks, page=0)
    search_msg = await message.answer(
        f"<b>🎵 Найдено {len(tracks)} треков</b>\n\nВыберите трек для скачивания 👇",
        parse_mode="HTML",
        reply_markup=keyboard
    )
    
    # Сохраняем сообщение с результатами поиска
    search_messages[user_id] = search_msg

# Запуск бота
async def main():
    logger.info("Бот запущен")
    logger.info("Режим skip_updates активирован: старые сообщения игнорируются")
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main()) 