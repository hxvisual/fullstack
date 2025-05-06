import React from 'react';
import './App.css';
import About from './components/About';
import Features from './components/Features';
import Footer from './components/Footer';
import Header from './components/Header';
import Hero from './components/Hero';
import HowTo from './components/HowTo';

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <Hero />
        <Features />
        <HowTo />
        <About />
      </main>
      <Footer />
    </div>
  );
}

export default App; 