import React from 'react';
import './HowTo.css';

const HowTo = () => {
  return (
    <section id="how-to" className="how-to">
      <div className="container">
        <h2>Как пользоваться HX Music Bot</h2>
        <div className="steps-container">
          <div className="step">
            <div className="step-number">1</div>
            <div className="step-content">
              <h3>Откройте бота в Telegram</h3>
              <p>Нажмите на кнопку "Открыть в Telegram" или найдите @hxmusic_robot в поиске Telegram</p>
            </div>
          </div>
          
          <div className="step">
            <div className="step-number">2</div>
            <div className="step-content">
              <h3>Напишите название песни</h3>
              <p>Просто отправьте сообщение с названием песни или именем исполнителя, который вы хотите найти</p>
            </div>
          </div>
          
          <div className="step">
            <div className="step-number">3</div>
            <div className="step-content">
              <h3>Выберите нужный трек</h3>
              <p>Из списка найденных песен выберите ту, которую хотите скачать</p>
            </div>
          </div>
          
          <div className="step">
            <div className="step-number">4</div>
            <div className="step-content">
              <h3>Получите музыку мгновенно</h3>
              <p>Бот автоматически загрузит и отправит вам песню в виде аудиофайла</p>
            </div>
          </div>
        </div>
        
        <div className="action-button">
          <a 
            href="https://t.me/hxmusic_robot" 
            className="btn btn-primary"
            target="_blank"
            rel="noopener noreferrer"
          >
            Начать прямо сейчас
          </a>
        </div>
      </div>
    </section>
  );
};

export default HowTo; 