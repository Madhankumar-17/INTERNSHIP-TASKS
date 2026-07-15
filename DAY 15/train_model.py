import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("smart_traffic_management_dataset.csv")

# Convert timestamp to datetime and extract useful features
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour
df["day"] = df["timestamp"].dt.day
df.drop("timestamp", axis=1, inplace=True)

# Encode weather
le = LabelEncoder()
df["weather_condition"] = le.fit_transform(df["weather_condition"])

# Features and target
X = df[[
    "location_id",
    "traffic_volume",
    "avg_vehicle_speed",
    "vehicle_count_cars",
    "vehicle_count_trucks",
    "vehicle_count_bikes",
    "temperature",
    "humidity"
]]
y = df["signal_status"]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_scaled, y)

# Save model
with open("traffic_logistic_randomsearch.pkl", "wb") as f:
    pickle.dump(model, f)

# Save scaler
with open("traffic_scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model and scaler saved successfully!")
print("Number of features:", X.shape[1])
print("Feature names:", list(X.columns))