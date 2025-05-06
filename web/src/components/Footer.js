import React from 'react';
import './Footer.css';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-logo">
            <span className="logo-icon">🎵</span>
            <span className="logo-text">HX Music Bot</span>
            <p className="footer-tagline">Ваша музыка всегда под рукой</p>
          </div>
          
          <div className="footer-links">
            <div className="footer-links-column">
              <h3>Навигация</h3>
            <ul>
                <li><a href="#home">Главная</a></li>
              <li><a href="#features">Возможности</a></li>
                <li><a href="#how-to">Как пользоваться</a></li>
              <li><a href="#about">О боте</a></li>
              </ul>
            </div>
            
            <div className="footer-links-column">
              <h3>Контакты</h3>
              <ul>
                <li><a href="https://t.me/hxmusic_robot" target="_blank" rel="noopener noreferrer">Telegram</a></li>
                <li><a href="mailto:support@hxmusicbot.com">Поддержка</a></li>
              </ul>
            </div>
            
            <div className="footer-links-column">
              <h3>Правовая информация</h3>
              <ul>
                <li><a href="#privacy">Политика конфиденциальности</a></li>
                <li><a href="#terms">Условия использования</a></li>
            </ul>
          </div>
          </div>
        </div>
        
        <div className="footer-decoration">
          <div className="footer-glow"></div>
        </div>
        
        <div className="footer-bottom">
          <p>&copy; {currentYear} HX Music Bot. Все права защищены.</p>
          <p className="disclaimer">
            HX Music Bot не хранит музыкальные файлы. Бот предоставляет доступ к музыке из открытых источников.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 