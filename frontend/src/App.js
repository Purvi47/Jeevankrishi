import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import CropRecommendation from './pages/CropRecommendation';
import FertilizerRecommendation from './pages/FertilizerRecommendation';
import Weather from './pages/Weather';
import News from './pages/News';

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/crop-recommendation" element={<CropRecommendation />} />
        <Route path="/fertilizer" element={<FertilizerRecommendation />} />
        <Route path="/weather" element={<Weather />} />
        <Route path="/news" element={<News />} />

      </Routes>
    </Router>
  );
};

export default App;

