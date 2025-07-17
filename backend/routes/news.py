from flask import Blueprint, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

news_bp = Blueprint('news', __name__)
API_KEY = os.getenv("NEWS_API_KEY")  

RELEVANT_KEYWORDS = [
    'farmer', 'farming', 'crop', 'mandi', 'pm-kisan', 'irrigation',
    'fertilizer', 'rainfall', 'monsoon', 'harvest', 'agriculture',
    'soil', 'kisan', 'weather', 'organic', 'seeds', 'yield'
]

BLOCKED_KEYWORDS = ['camera', 'sensor', 'sony', 'smartphone', 'lens', 'gadget']

def is_relevant(article):
    if not isinstance(article, dict):
        return False
    title = (article.get('title') or '').lower()
    description = (article.get('description') or '').lower()
    combined = title + ' ' + description

    if any(bad in combined for bad in BLOCKED_KEYWORDS):
        return False

    return any(good in combined for good in RELEVANT_KEYWORDS)

@news_bp.route('/', methods=['GET'])
def get_agriculture_news():
    query = "agriculture OR farmer OR crop OR mandi OR irrigation"
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&q={query}&country=in&language=en"

    try:
        response = requests.get(url)
        data = response.json()
        results = data.get('results', [])

        filtered_articles = []
        for article in results:
            if is_relevant(article):
                filtered_articles.append({
                    'title': article.get('title', 'No title'),
                    'description': article.get('description') or 'No description',
                    'url': article.get('link', '#'),
                    'source': article.get('source_id', 'Unknown'),
                    'pubDate': article.get('pubDate', '')
                })
            if len(filtered_articles) == 6:
                break

        if not filtered_articles:
            return jsonify({'error': 'No agriculture news found'}), 404

        return jsonify({'articles': filtered_articles})

    except Exception as e:
        return jsonify({'error': str(e)}), 500
