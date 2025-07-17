from flask import Blueprint, request, jsonify
import pickle
import os
import numpy as np

fertilizer_bp = Blueprint("fertilizer", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
model_path = os.path.join(ROOT_DIR, "ml_models", "fertilizer_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

@fertilizer_bp.route("/fertilizer-recommend", methods=["POST"])
def recommend_fertilizer():
    try:
        data = request.get_json()
        input_data = [
            float(data["N"]),
            float(data["P"]),
            float(data["K"])
        ]

        prediction = model.predict([input_data])[0]
        return jsonify({"recommended_fertilizer": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})
