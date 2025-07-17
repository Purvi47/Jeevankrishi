import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

# 📥 Load dataset
df = pd.read_csv("data/Crop_recommendation.csv")

# 🧠 Features and labels
X = df.drop("label", axis=1)
y = df["label"]

# 📊 Split into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🌲 Train RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 💾 Save model to backend/ml_models
model_dir = os.path.join("ml_models")
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, "crop_recommender.pkl")
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Model trained and saved at {model_path}")
