from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_keyboard():
    """
    Создает основную клавиатуру с доступными командами
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="ℹ️ Помощь"),
                KeyboardButton(text="👋 О боте")
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

def get_track_inline_keyboard(track):
    """
    Создает инлайн-клавиатуру для взаимодействия с треком
    """
    builder = InlineKeyboardBuilder()
    
    # Кнопка для прослушивания превью, если доступно
    if track.get('preview_url'):
        builder.add(
            InlineKeyboardButton(
                text="🎵 Прослушать превью",
                url=track['preview_url']
            )
        )
    
    # Кнопка для открытия в Spotify
    builder.add(
        InlineKeyboardButton(
            text="🎧 Открыть в Spotify",
            url=track['external_url']
        )
    )
    
    # Добавление кнопки для получения похожих треков
    if 'id' in track:
        builder.add(
            InlineKeyboardButton(
                text="👍 Похожие треки",
                callback_data=f"similar:{track['id']}"
            )
        )
    
    # Кнопка для нового поиска
    builder.add(
        InlineKeyboardButton(
            text="🔍 Новый поиск",
            callback_data="new_search"
        )
    )
    
    # Настройка сетки кнопок
    builder.adjust(1)
    
    return builder.as_markup()

def get_search_results_keyboard(tracks, page=0, page_size=5):
    """
    Создает инлайн-клавиатуру для отображения результатов поиска
    
    Args:
        tracks (list): Список треков
        page (int): Текущая страница
        page_size (int): Количество треков на странице
        
    Returns:
        InlineKeyboardMarkup: Клавиатура с результатами поиска
    """
    builder = InlineKeyboardBuilder()
    
    # Расчет параметров пагинации
    total_pages = (len(tracks) + page_size - 1) // page_size if tracks else 0
    start_idx = page * page_size
    end_idx = min(start_idx + page_size, len(tracks)) if tracks else 0
    
    # Добавляем кнопки с треками
    if tracks:
        for i in range(start_idx, end_idx):
            track = tracks[i]
            track_name = track['name']
            artist = track['artist']
            
            # Ограничиваем длину текста кнопки
            button_text = f"{i+1}. {track_name} - {artist}"
            if len(button_text) > 60:
                button_text = button_text[:57] + "..."
            
            builder.add(
                InlineKeyboardButton(
                    text=button_text,
                    callback_data=f"track:{i}"
                )
            )
    
    # Добавляем навигационные кнопки
    if total_pages > 1:
        row = []
        if page > 0:
            row.append(InlineKeyboardButton(
                text="◀️ Назад",
                callback_data=f"page:{page-1}"
            ))
        
        if page < total_pages - 1:
            row.append(InlineKeyboardButton(
                text="▶️ Вперед",
                callback_data=f"page:{page+1}"
            ))
        
        builder.row(*row)
    
    # Настройка сетки кнопок - по одной кнопке в ряду для треков
    builder.adjust(1)
    
    return builder.as_markup() 