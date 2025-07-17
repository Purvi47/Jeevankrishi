import React from 'react';
import '../styles/Home.css';
import heroImage from '../assets/sunny-meadow-landscape.jpg';
const Home = () => {
  return (
    <div className="home">
      <section className="hero-image">
        <img src={heroImage} alt="Sunny meadow landscape" />
      </section>

      <section className="features">
        <h2>🔧 What We Offer</h2>
        <div className="feature-grid">
          <div className="feature-card">
            <h3>🌾 Crop Recommendation</h3>
            <p>Get crop suggestions based on soil nutrients and climate.</p>
          </div>
          <div className="feature-card">
            <h3>🧪 Fertilizer Suggestion</h3>
            <p>Get AI-based fertilizer recommendations to boost yield.</p>
          </div>
          <div className="feature-card">
            <h3>🦠 Disease Detection (Coming Soon)</h3>
            <p>Upload leaf images to identify crop diseases using AI.</p>
          </div>
        </div>
      </section>

      <footer className="footer">
        <p>© 2025 JeevanKrishi | Built with ❤️ for Indian farmers</p>
      </footer>
    </div>
  );
};

export default Home;
