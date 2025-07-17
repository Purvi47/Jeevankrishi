import React, { useState } from 'react';
import '../styles/CommonPage.css';

const FertilizerRecommendation = () => {
  const [formData, setFormData] = useState({
    temperature: '', humidity: '', moisture: '',
    soilType: '', cropType: '', nitrogen: '',
    phosphorous: '', potassium: ''
  });

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    console.log("Submitted Data:", formData);
  };

  return (
    <div className="form-page">
      <h2>🧪 Fertilizer Recommendation</h2>
      <form className="form-grid" onSubmit={handleSubmit}>
        {Object.entries(formData).map(([key, val]) => (
          <input
            key={key}
            name={key}
            type="text"
            placeholder={key}
            value={val}
            onChange={handleChange}
            required
          />
        ))}
        <button type="submit">🌱 Get Recommendation</button>
      </form>
    </div>
  );
};

export default FertilizerRecommendation;
