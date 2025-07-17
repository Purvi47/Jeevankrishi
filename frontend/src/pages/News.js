import React, { useEffect, useState } from 'react';
import '../styles/News.css';
import { api } from '../api/api'; // ✅ Named import

const News = () => {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    api.get('/api/news') // ✅ Uses named axios instance
      .then(res => setArticles(res.data.articles))
      .catch(err => console.error('Error loading news:', err));
  }, []);

  return (
    <div className="news-container">
      <h2>📰 Agriculture News & Alerts</h2>
      {articles.map((a, i) => (
        <a key={i} className="news-card" href={a.url} target="_blank" rel="noreferrer">
          <h3>{a.title}</h3>
          <p>{a.description}</p>
          <div className="source">{a.source}</div>
        </a>
      ))}
    </div>
  );
};

export default News;
