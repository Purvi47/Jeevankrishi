import React, { useState } from 'react';
import '../styles/CommonPage.css';

const CropRecommendation = () => {
  const [formData, setFormData] = useState({
    N: '', P: '', K: '', temperature: '', humidity: '', ph: '', rainfall: ''
  });

  const handleChange = e => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    // Add API logic here
    console.log("Submitted Data:", formData);
  };

  return (
    <div className="form-page">
      <h2>🌿 Crop Recommendation</h2>
      <form className="form-grid" onSubmit={handleSubmit}>
        {Object.entries(formData).map(([key, val]) => (
          <input
            key={key}
            name={key}
            type="number"
            placeholder={key.charAt(0).toUpperCase() + key.slice(1)}
            value={val}
            onChange={handleChange}
            required
          />
        ))}
        <button type="submit">🌾 Get Recommendation</button>
      </form>
    </div>
  );
};

export default CropRecommendation;
