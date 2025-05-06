import React from 'react';
import './Hero.css';

const Hero = () => {
  return (
    <section className="hero">
      <div className="hero-decoration">
        <div className="decoration-circle"></div>
        <div className="decoration-circle"></div>
        <div className="decoration-circle"></div>
      </div>
      
      <div className="container">
        <div className="hero-content">
          <h2>HX Music Bot</h2>
          <p className="hero-tagline">Ваша музыка всегда под рукой</p>
          <p>Мгновенный поиск и скачивание любимых треков прямо в Telegram без рекламы и ограничений</p>
          <div className="cta-buttons">
            <a 
              href="https://t.me/hxmusic_robot" 
              className="btn btn-primary"
              target="_blank"
              rel="noopener noreferrer"
            >
              Открыть в Telegram
            </a>
            <a href="#how-to" className="btn btn-secondary">Как пользоваться</a>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero; 