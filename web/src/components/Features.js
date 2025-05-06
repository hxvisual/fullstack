import React from 'react';
import './Features.css';

const Features = () => {
  return (
    <section id="features" className="features">
      <div className="container">
        <h2>Возможности HX Music Bot</h2>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">🔍</div>
            <h3>Мгновенный поиск</h3>
            <p>Найдите любую песню за считанные секунды по названию или имени исполнителя</p>
          </div>
          
          <div className="feature-card">
            <div className="feature-icon">📥</div>
            <h3>Скачивание без ограничений</h3>
            <p>Получите полные версии треков в высоком качестве без лимитов и подписок</p>
          </div>
          
          <div className="feature-card">
            <div className="feature-icon">🎧</div>
            <h3>Прямо в Telegram</h3>
            <p>Слушайте музыку прямо в мессенджере или скачивайте для прослушивания офлайн</p>
          </div>
          
          <div className="feature-card">
            <div className="feature-icon">⚡</div>
            <h3>Молниеносная скорость</h3>
            <p>Бот работает максимально быстро - никаких долгих загрузок или ожиданий</p>
          </div>
          
          <div className="feature-card">
            <div className="feature-icon">🔐</div>
            <h3>Полная безопасность</h3>
            <p>Ваши данные надежно защищены, никаких регистраций или личной информации</p>
          </div>
          
          <div className="feature-card">
            <div className="feature-icon">👍</div>
            <h3>Простой интерфейс</h3>
            <p>Интуитивно понятное управление без лишних кнопок и сложных команд</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Features; 