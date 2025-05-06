import React from 'react';
import './HowTo.css';

const HowTo = () => {
  const steps = [
    {
      id: 1,
      title: 'Найдите бота в Telegram',
      description: 'Перейдите по ссылке t.me/your_bot_username или найдите бота по имени в поиске Telegram.',
      number: '1'
    },
    {
      id: 2,
      title: 'Нажмите кнопку "Старт"',
      description: 'Запустите бота, нажав кнопку /start или введя команду /start в чате.',
      number: '2'
    },
    {
      id: 3,
      title: 'Используйте команды',
      description: 'Взаимодействуйте с ботом, используя доступные команды, такие как /help для помощи.',
      number: '3'
    }
  ];

  return (
    <section id="howto" className="howto">
      <div className="container">
        <h2 className="section-title">Как использовать бота</h2>
        <div className="steps">
          {steps.map(step => (
            <div className="step" key={step.id}>
              <div className="step-number">{step.number}</div>
              <div className="step-content">
                <h3>{step.title}</h3>
                <p>{step.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default HowTo; 