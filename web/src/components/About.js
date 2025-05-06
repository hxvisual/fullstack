import React from 'react';
import './About.css';

const About = () => {
  return (
    <section id="about" className="about">
      <div className="container">
        <h2>О нашем боте</h2>
        <p className="about-tagline">HX Music Bot — ваш идеальный музыкальный компаньон в Telegram</p>
        
        <div className="about-content">
          <div className="about-text">
            <p>
              Мы создали HX Music Bot, чтобы сделать доступ к любимой музыке максимально простым и быстрым.
              Наш бот позволяет мгновенно находить и скачивать любые треки прямо в Telegram без необходимости
              перехода на сторонние сервисы, регистрации или оплаты подписок.
            </p>
            <p>
              Просто отправьте название песни или имя исполнителя, и бот сделает всю работу за вас —
              найдет лучшее совпадение и автоматически начнет загрузку полной версии трека в высоком качестве.
              Никакой рекламы, ограничений по времени или количеству скачиваний.
            </p>
          </div>
          
          <div className="about-decoration">
            <div className="decoration-element"></div>
            <div className="decoration-element"></div>
            <div className="decoration-element"></div>
          </div>
        </div>
        
        <div className="stats">
          <div className="stat">
            <span className="stat-number">0</span>
            <span className="stat-label">Треков доступно</span>
          </div>
          <div className="stat">
            <span className="stat-number">0</span>
            <span className="stat-label">Активных пользователей</span>
          </div>
          <div className="stat">
            <span className="stat-number">24/7</span>
            <span className="stat-label">Работаем без перерывов</span>
          </div>
        </div>
        
        <div className="cta-container">
          <a href="https://t.me/hxmusic_robot" className="btn btn-primary" target="_blank" rel="noopener noreferrer">
            Открыть бота <i className="bx bx-right-arrow-alt"></i>
          </a>
        </div>
      </div>
    </section>
  );
};

export default About; 