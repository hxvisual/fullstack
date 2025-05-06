#!/bin/bash

# Выводим информацию о процессе деплоя
echo "Начинаем процесс деплоя..."
date

# Переходим в директорию проекта
cd /var/www/bot.hxvisual.ru

# Активируем виртуальное окружение Python для бота
cd bot
echo "Обновляем зависимости Python..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Перезапускаем сервис бота
echo "Перезапускаем сервис бота..."
sudo systemctl restart telegram-bot.service

# Переходим в директорию веб-приложения и обновляем зависимости
cd ../web
echo "Обновляем зависимости Node.js..."
npm install

# Собираем React-приложение
echo "Собираем React-приложение..."
npm run build

# Обновляем Nginx
echo "Перезапускаем Nginx..."
sudo systemctl restart nginx

echo "Деплой успешно завершен."
date 