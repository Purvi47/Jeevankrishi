import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

df = pd.read_csv("data/Fertilizer Prediction.csv")  

print("Columns in the dataset:", df.columns)

df.rename(columns={"Fertilizer Name": "fertilizer_name"}, inplace=True)

le_soil = LabelEncoder()
le_crop = LabelEncoder()
le_fert = LabelEncoder()

df["Soil Type"] = le_soil.fit_transform(df["Soil Type"])
df["Crop Type"] = le_crop.fit_transform(df["Crop Type"])
df["fertilizer_name"] = le_fert.fit_transform(df["fertilizer_name"])


X = df.drop("fertilizer_name", axis=1)
y = df["fertilizer_name"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

os.makedirs("ml_models", exist_ok=True)
with open("ml_models/fertilizer_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Fertilizer model trained and saved at ml_models/fertilizer_model.pkl")
