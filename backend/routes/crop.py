from flask import Blueprint, request, jsonify
import pickle
import numpy as np
import os

crop_bp = Blueprint("crop", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  
ROOT_DIR = os.path.dirname(BASE_DIR)  
model_path = os.path.join(ROOT_DIR, "ml_models", "crop_recommender.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

@crop_bp.route("/crop-recommend", methods=["POST"])
def recommend_crop():
    try:
        data = request.get_json()

        input_data = [
            float(data["N"]),
            float(data["P"]),
            float(data["K"]),
            float(data["temperature"]),
            float(data["humidity"]),
            float(data["ph"]),
            float(data["rainfall"]),
        ]

        prediction = model.predict([input_data])[0]
        return jsonify({"recommended_crop": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})
