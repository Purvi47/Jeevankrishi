from flask import Blueprint, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

weather_bp = Blueprint('weather', __name__)
API_KEY = os.getenv("WEATHER_API_KEY") 

@weather_bp.route('/', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    print(f"Fetching URL: {url}")

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != "200":
            return jsonify({'error': data.get('message', 'Weather API error')}), 500

        forecast = []
        for item in data['list'][:5]:
            forecast.append({
                'datetime': item['dt_txt'],
                'temp': item['main']['temp'],
                'weather': item['weather'][0]['description']
            })

        return jsonify({'city': city, 'forecast': forecast})

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500
