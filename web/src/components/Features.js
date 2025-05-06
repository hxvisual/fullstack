import React from 'react';
import './Features.css';

const Features = () => {
  const features = [
    {
      id: 1,
      title: 'Быстрые ответы',
      description: 'Мгновенные ответы на ваши запросы в любое время дня и ночи.',
      icon: '⚡'
    },
    {
      id: 2,
      title: 'Простое использование',
      description: 'Интуитивно понятный интерфейс и команды для удобного взаимодействия.',
      icon: '🔍'
    },
    {
      id: 3,
      title: 'Персонализация',
      description: 'Настройте бота под свои потребности и предпочтения.',
      icon: '⚙️'
    }
  ];

  return (
    <section id="features" className="features">
      <div className="container">
        <h2 className="section-title">Возможности бота</h2>
        <div className="features-grid">
          {features.map(feature => (
            <div className="feature-card" key={feature.id}>
              <div className="feature-icon">{feature.icon}</div>
              <h3>{feature.title}</h3>
              <p>{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features; 