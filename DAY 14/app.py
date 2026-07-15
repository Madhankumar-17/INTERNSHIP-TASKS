import os

from flask import Flask, render_template, request
import sqlite3
import matplotlib.pyplot as plt
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("traffic_logistic_randomsearch.pkl", "rb") as f:
    model = pickle.load(f)

# Load scaler
with open("traffic_scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Print after loading
print("Scaler expects", scaler.n_features_in_, "features")
prediction_history = []
def generate_chart():
    conn = sqlite3.connect("traffic.db")
    cursor = conn.cursor()

    cursor.execute("SELECT prediction, COUNT(*) FROM predictions GROUP BY prediction")
    data = cursor.fetchall()

    conn.close()

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    plt.figure(figsize=(5,5))
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Traffic Prediction Distribution")
    os.makedirs("static/charts", exist_ok=True)
    plt.savefig("static/charts/pie_chart.png")
    plt.close()
@app.route("/")
def home():
    conn = sqlite3.connect("traffic.db")
    cursor = conn.cursor()

    # Total predictions
    cursor.execute("SELECT COUNT(*) FROM predictions")
    total = cursor.fetchone()[0]

    # High traffic predictions
    cursor.execute("SELECT COUNT(*) FROM predictions WHERE prediction='High Traffic'")
    high = cursor.fetchone()[0]

    # Low traffic predictions
    cursor.execute("SELECT COUNT(*) FROM predictions WHERE prediction='Low Traffic'")
    low = cursor.fetchone()[0]

    # Latest prediction
    cursor.execute("SELECT prediction FROM predictions ORDER BY id DESC LIMIT 1")
    latest = cursor.fetchone()

    conn.close()

    generate_chart()
    return render_template(
        "index.html",
        history=prediction_history,
        total=total,
        high=high,
        low=low,
        latest=latest[0] if latest else "No Data"
    )
@app.route("/predict", methods=["POST"])
def predict():
    try:
        location_id = float(request.form["location_id"])
        traffic_volume = float(request.form["traffic_volume"])
        avg_vehicle_speed = float(request.form["avg_vehicle_speed"])
        vehicle_count_cars = float(request.form["vehicle_count_cars"])
        vehicle_count_trucks = float(request.form["vehicle_count_trucks"])
        vehicle_count_bikes = float(request.form["vehicle_count_bikes"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])

        data = np.array([[location_id,
                          traffic_volume,
                          avg_vehicle_speed,
                          vehicle_count_cars,
                          vehicle_count_trucks,
                          vehicle_count_bikes,
                          temperature,
                          humidity]])

        data = scaler.transform(data)
        prediction = model.predict(data)

        # Save prediction to SQLite
        conn = sqlite3.connect("traffic.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO predictions (location_id, traffic_volume, prediction) VALUES (?, ?, ?)",
            (location_id, traffic_volume, str(prediction[0]))
        )

        conn.commit()
        conn.close()

        # Save prediction to history
        prediction_history.append({
            "location": location_id,
            "traffic": traffic_volume,
            "speed": avg_vehicle_speed,
            "prediction": prediction[0]
        })

        return render_template(
            "index.html",
            prediction_text=f"Prediction: {prediction[0]}",
            history=prediction_history
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {e}",
            history=prediction_history
        )
@app.route("/history")
def history():
    conn = sqlite3.connect("traffic.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()

    return render_template("history.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)