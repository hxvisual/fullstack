import React from 'react';
import './Hero.css';

const Hero = () => {
  return (
    <section className="hero">
      <div className="container">
        <div className="hero-content">
          <h2>Ваш персональный Telegram бот</h2>
          <p>Простой, быстрый и удобный помощник для ваших задач</p>
          <div className="cta-buttons">
            <a 
              href="https://t.me/your_bot_username" 
              className="btn btn-primary"
              target="_blank"
              rel="noopener noreferrer"
            >
              Начать общение
            </a>
            <a href="#features" className="btn btn-secondary">Узнать больше</a>
          </div>
        </div>
        <div className="hero-image">
          <img src="/images/bot-preview.png" alt="Превью бота" />
        </div>
      </div>
    </section>
  );
};

export default Hero; 