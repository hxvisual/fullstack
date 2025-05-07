#!/bin/bash

# Обновляем систему
echo "Обновляем систему..."
sudo apt update
sudo apt upgrade -y

# Устанавливаем необходимые зависимости
echo "Устанавливаем зависимости..."
sudo apt install -y python3 python3-pip python3-venv nodejs npm nginx certbot python3-certbot-nginx git

# Создаем директорию для проекта
echo "Создаем директорию проекта..."
sudo mkdir -p /var/www/bot.hxvisual.ru
sudo chown $USER:$USER /var/www/bot.hxvisual.ru

# Клонируем репозиторий
echo "Клонируем репозиторий..."
git clone https://github.com/hxvisual/fullstack.git /var/www/bot.hxvisual.ru

# Настраиваем бота
cd /var/www/bot.hxvisual.ru/bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Создаем файл окружения для бота
echo "Создаем файл окружения для бота..."
cat << EOF > .env
BOT_TOKEN=your_bot_token_here
ADMIN_ID=your_admin_telegram_id
SPOTIFY_CLIENT_ID=spotify_client_id
SPOTIFY_CLIENT_SECRET=spotify_client_secret
EOF

# Создаем сервис systemd для автозапуска бота
echo "Создаем сервис для бота..."
sudo tee /etc/systemd/system/telegram-bot.service << EOF
[Unit]
Description=Telegram Bot Service
After=network.target

[Service]
User=$USER
WorkingDirectory=/var/www/bot.hxvisual.ru/bot
ExecStart=/var/www/bot.hxvisual.ru/bot/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Запускаем и активируем сервис
sudo systemctl daemon-reload
sudo systemctl enable telegram-bot.service
sudo systemctl start telegram-bot.service

# Собираем React-приложение
cd /var/www/bot.hxvisual.ru/web
npm install
npm run build

# Настраиваем Nginx
echo "Настраиваем Nginx..."
sudo tee /etc/nginx/sites-available/bot.hxvisual.ru << EOF
server {
    listen 80;
    server_name bot.hxvisual.ru;
    root /var/www/bot.hxvisual.ru/web/build;
    index index.html;

    location / {
        try_files \$uri \$uri/ /index.html;
    }
}
EOF

# Активируем конфигурацию Nginx
sudo ln -s /etc/nginx/sites-available/bot.hxvisual.ru /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx

# Настраиваем SSL с помощью Let's Encrypt
echo "Настраиваем SSL..."
sudo certbot --nginx -d bot.hxvisual.ru --non-interactive --agree-tos --email your-email@example.com

echo "Установка завершена! Сайт и бот развернуты по адресу bot.hxvisual.ru" 