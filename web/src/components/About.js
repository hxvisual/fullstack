import React from 'react';
import './About.css';

const About = () => {
  return (
    <section id="about" className="about">
      <div className="container">
        <h2 className="section-title">О боте</h2>
        <div className="about-content">
          <div className="about-text">
            <p>
              Наш Telegram бот разработан с использованием современных технологий 
              для обеспечения быстрой и надежной работы. Бот использует Python и
              фреймворк aiogram для взаимодействия с Telegram API.
            </p>
            <p>
              Мы стремимся сделать бота максимально удобным и функциональным.
              Постоянно добавляем новые возможности и улучшаем существующий функционал
              на основе отзывов пользователей.
            </p>
            <p>
              Если у вас есть вопросы или предложения по улучшению бота, 
              пожалуйста, свяжитесь с нами через форму обратной связи или напрямую в Telegram.
            </p>
          </div>
          <div className="about-stats">
            <div className="stat">
              <div className="stat-value">24/7</div>
              <div className="stat-label">Доступность</div>
            </div>
            <div className="stat">
              <div className="stat-value">0.5s</div>
              <div className="stat-label">Среднее время ответа</div>
            </div>
            <div className="stat">
              <div className="stat-value">100%</div>
              <div className="stat-label">Защита данных</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About; 