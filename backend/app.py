from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)  

from routes.weather import weather_bp
from routes.crop import crop_bp
from routes.fertilizer import fertilizer_bp
from routes.news import news_bp

app.register_blueprint(weather_bp, url_prefix="/api/weather")
app.register_blueprint(crop_bp, url_prefix="/api/crop")
app.register_blueprint(fertilizer_bp, url_prefix="/api/fertilizer")
app.register_blueprint(news_bp, url_prefix="/api/news")

@app.route("/", methods=["GET"])
def home():
    return "🌾 JeevanKrishi Backend is Running Successfully!"

if __name__ == "__main__":
    app.run(debug=True)
