import os
import spotipy
import requests
import yt_dlp
from spotipy.oauth2 import SpotifyClientCredentials
from loguru import logger

class MusicService:
    def __init__(self):
        """
        Инициализация сервиса для поиска музыки через Spotify API.
        Требует SPOTIFY_CLIENT_ID и SPOTIFY_CLIENT_SECRET в переменных окружения.
        """
        try:
            client_id = os.getenv('SPOTIFY_CLIENT_ID')
            client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
            
            if not client_id or not client_secret:
                logger.error("Не найдены учетные данные Spotify API в переменных окружения")
                raise ValueError("Отсутствуют учетные данные Spotify API")
            
            client_credentials_manager = SpotifyClientCredentials(
                client_id=client_id, 
                client_secret=client_secret
            )
            self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
            logger.info("Spotify API клиент успешно инициализирован")
        except Exception as e:
            logger.error(f"Ошибка при инициализации Spotify API: {e}")
            raise
    
    async def search_track(self, query, limit=5):
        """
        Поиск трека по запросу.
        
        Args:
            query (str): Поисковый запрос
            limit (int): Максимальное количество результатов
            
        Returns:
            list: Список найденных треков с информацией
        """
        try:
            logger.info(f"Поиск трека: '{query}', лимит: {limit}")
            results = self.spotify.search(q=query, limit=limit, type='track')
            
            tracks = []
            for item in results['tracks']['items']:
                track_info = {
                    'name': item['name'],
                    'artist': ', '.join([artist['name'] for artist in item['artists']]),
                    'album': item['album']['name'],
                    'release_date': item['album']['release_date'],
                    'duration_ms': item['duration_ms'],
                    'popularity': item['popularity'],
                    'preview_url': item['preview_url'],
                    'external_url': item['external_urls']['spotify'],
                    'image_url': item['album']['images'][0]['url'] if item['album']['images'] else None,
                    'id': item['id']
                }
                tracks.append(track_info)
            
            logger.info(f"Найдено {len(tracks)} треков")
            return tracks
        except Exception as e:
            logger.error(f"Ошибка при поиске трека: {e}")
            return []
    
    async def get_track_recommendations(self, track_id, limit=5):
        """
        Получение рекомендаций на основе трека.
        
        Args:
            track_id (str): ID трека в Spotify
            limit (int): Максимальное количество рекомендаций
            
        Returns:
            list: Список рекомендованных треков
        """
        try:
            logger.info(f"Получение рекомендаций для трека ID: {track_id}")
            recommendations = self.spotify.recommendations(seed_tracks=[track_id], limit=limit)
            
            tracks = []
            for item in recommendations['tracks']:
                track_info = {
                    'name': item['name'],
                    'artist': ', '.join([artist['name'] for artist in item['artists']]),
                    'album': item['album']['name'],
                    'preview_url': item['preview_url'],
                    'external_url': item['external_urls']['spotify'],
                    'image_url': item['album']['images'][0]['url'] if item['album']['images'] else None
                }
                tracks.append(track_info)
            
            return tracks
        except Exception as e:
            logger.error(f"Ошибка при получении рекомендаций: {e}")
            return []
    
    def format_track_info(self, track):
        """
        Форматирование информации о треке для отображения в сообщении.
        
        Args:
            track (dict): Информация о треке
            
        Returns:
            str: Форматированный текст
        """
        duration_sec = track['duration_ms'] // 1000
        minutes = duration_sec // 60
        seconds = duration_sec % 60
        
        text = (
            f"🎵 <b>{track['name']}</b>\n"
            f"🎤 Исполнитель: {track['artist']}\n"
            f"💿 Альбом: {track['album']}\n"
            f"📅 Дата выхода: {track['release_date']}\n"
            f"⏱ Длительность: {minutes}:{seconds:02d}\n"
            f"🔗 <a href='{track['external_url']}'>Слушать на Spotify</a>"
        )
        
        return text
        
    async def download_full_song(self, track):
        """
        Загрузка полной песни с YouTube.
        
        Args:
            track (dict): Информация о треке
            
        Returns:
            str: Путь к загруженному файлу или None
        """
        try:
            search_query = f"{track['name']} {track['artist']}"
            logger.info(f"Загрузка полной песни: '{search_query}'")
            
            # Убедимся, что директория существует
            downloads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')
            os.makedirs(downloads_dir, exist_ok=True)
            
            # Безопасное имя файла
            safe_filename = f"{track['artist']} - {track['name']}".replace('/', '_').replace('\\', '_')
            safe_filename = ''.join(c for c in safe_filename if c.isalnum() or c in ' -_.')
            output_file = os.path.join(downloads_dir, f"{safe_filename}.mp3")
            
            # Проверяем, существует ли файл уже
            if os.path.exists(output_file):
                logger.info(f"Файл уже существует: {output_file}")
                return output_file
            
            # Опции для yt-dlp
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': output_file,
                'noplaylist': True,
                'quiet': True,
                'no_warnings': True,
                'ignoreerrors': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            
            # Загрузка песни
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    info = ydl.extract_info(f"ytsearch:{search_query}", download=True)
                    if info and 'entries' in info and info['entries']:
                        logger.info(f"Песня успешно загружена: {output_file}")
                        return output_file
                    else:
                        logger.error(f"Не удалось найти песню: {search_query}")
                        return None
                except Exception as e:
                    logger.error(f"Ошибка при загрузке с YouTube: {e}")
                    return None
            
            return None
        except Exception as e:
            logger.error(f"Ошибка при загрузке полной песни: {e}")
            return None 