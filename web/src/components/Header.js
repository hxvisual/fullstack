import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="container">
        <div className="logo">
          <img src="/logo192.png" alt="Логотип бота" width="40" height="40" />
          <h1>Telegram Бот</h1>
        </div>
        <nav className="nav">
          <ul>
            <li><a href="#features">Возможности</a></li>
            <li><a href="#howto">Как использовать</a></li>
            <li><a href="#about">О боте</a></li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header; 