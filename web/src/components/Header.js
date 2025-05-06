import React, { useState } from 'react';
import './Header.css';

const Header = () => {
  const [menuOpen, setMenuOpen] = useState(false);
  
  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };
  
  const closeMenu = () => {
    setMenuOpen(false);
  };
  
  return (
    <header className="header">
      <div className="container">
        <div className="logo">
          <div className="logo-icon">♫</div>
          <span className="logo-text">HX Music Bot</span>
        </div>
        
        <button className="mobile-menu-btn" onClick={toggleMenu}>
          <span>☰</span>
        </button>
        
        <nav className={`nav ${menuOpen ? 'active' : ''}`}>
          {menuOpen && (
            <button className="nav-close" onClick={closeMenu}>
              ✕
            </button>
          )}
          <ul className="nav-list">
            <li><a href="#features" onClick={closeMenu}>Возможности</a></li>
            <li><a href="#how-to" onClick={closeMenu}>Инструкция</a></li>
            <li><a href="#about" onClick={closeMenu}>О боте</a></li>
            <li>
              <a 
                href="https://t.me/hxmusic_robot" 
                className="btn btn-primary header-cta"
                target="_blank"
                rel="noopener noreferrer"
                onClick={closeMenu}
              >
                <span className="telegram-icon">✈️</span> Открыть в Telegram
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header; 