import React, { useState } from 'react';
import '../styles/Weather.css';
import { api } from '../api/api'; // ✅ Named import

const Weather = () => {
  const [city, setCity] = useState('');
  const [forecast, setForecast] = useState([]);

  const fetchWeather = async () => {
    try {
      const res = await api.get(`/api/weather?city=${city}`); // ✅ Use named api instance
      setForecast(res.data.forecast);
    } catch (err) {
      alert('Error fetching weather. Check city name or backend.');
    }
  };

  return (
    <div className="weather-container">
      <h2>🌦️ Weather Forecast</h2>
      <input
        type="text"
        value={city}
        onChange={e => setCity(e.target.value)}
        placeholder="Enter city name"
      />
      <button onClick={fetchWeather}>Get Forecast</button>

      <div className="forecast-grid">
        {forecast.map((item, idx) => (
          <div className="forecast-card" key={idx}>
            <h4>{item.datetime}</h4>
            <p>{item.temp}°C</p>
            <p>{item.weather}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Weather;
