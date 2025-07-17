import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">🌾 JeevanKrishi</div>
      <ul className="nav-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/crop-recommendation">Crop Recommendation</Link></li>
        <li><Link to="/fertilizer">Fertilizer Recommendation</Link></li>
        <Link to="/weather">Weather</Link>
        <Link to="/news"><button className="hero-button">📢 News</button></Link>


      </ul>
    </nav>
  );
};

export default Navbar;
