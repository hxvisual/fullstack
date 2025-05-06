import React from 'react';
import './Footer.css';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-info">
            <h3>Telegram Bot</h3>
            <p>Ваш персональный помощник на каждый день</p>
          </div>
          <div className="footer-links">
            <h4>Полезные ссылки</h4>
            <ul>
              <li><a href="#features">Возможности</a></li>
              <li><a href="#howto">Как использовать</a></li>
              <li><a href="#about">О боте</a></li>
              <li><a href="https://t.me/your_bot_username" target="_blank" rel="noopener noreferrer">Открыть в Telegram</a></li>
            </ul>
          </div>
          <div className="footer-contact">
            <h4>Контакты</h4>
            <p>Email: <a href="mailto:contact@example.com">contact@example.com</a></p>
            <p>Telegram: <a href="https://t.me/your_username" target="_blank" rel="noopener noreferrer">@your_username</a></p>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; {currentYear} Telegram Bot. Все права защищены.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 