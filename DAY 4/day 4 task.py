print("THIS IS A NEW CODE")

# ==============================================
# TrafficIQ - Smart Traffic & Congestion Predictor
# Part 1 (Tasks 1 to 4)
# Dataset: smart_traffic_management_dataset.csv
# ==============================================

import pandas as pd
import matplotlib.pyplot as plt
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# ==============================================
# Load Dataset
# ==============================================

import os

print("Current Folder:", os.getcwd())
print("Files:", os.listdir())
from pathlib import Path
import pandas as pd

file_path = Path(__file__).parent / "smart_traffic_management_dataset.csv"

df = pd.read_csv(file_path)

print("\nFirst 5 Records")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nDataset Information")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

# ==============================================
# Data Preprocessing
# ==============================================

# Convert categorical columns into numeric values

df["weather_condition"] = df["weather_condition"].astype("category").cat.codes

df["signal_status"] = df["signal_status"].astype("category").cat.codes

# Create Target Variable
# 0 = Low Traffic
# 1 = High Traffic (Congestion)

df["Congestion"] = (
    df["traffic_volume"] >
    df["traffic_volume"].median()
).astype(int)

print("\nCongestion Distribution")
print(df["Congestion"].value_counts())

# ==============================================
# TASK 1
# Data Visualization
# ==============================================

# -------------------------
# Bar Chart
# -------------------------

plt.figure(figsize=(6,4))

df["Congestion"].value_counts().plot(
    kind="bar",
    color=["green","red"]
)

plt.title("Traffic Congestion Distribution")
plt.xlabel("Congestion")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("traffic_bar.png")

plt.show()

# -------------------------
# Scatter Plot
# -------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    df["traffic_volume"],
    df["avg_vehicle_speed"],
    color="blue"
)

plt.title("Traffic Volume vs Average Speed")
plt.xlabel("Traffic Volume")
plt.ylabel("Average Speed")

plt.tight_layout()

plt.savefig("traffic_scatter.png")

plt.show()

# -------------------------
# Histogram
# -------------------------

plt.figure(figsize=(6,4))

plt.hist(
    df["traffic_volume"],
    bins=15,
    color="orange"
)

plt.title("Traffic Volume Distribution")
plt.xlabel("Traffic Volume")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("traffic_histogram.png")

plt.show()

# -------------------------
# Line Chart
# -------------------------

plt.figure(figsize=(8,4))

plt.plot(
    df["traffic_volume"],
    marker="o"
)

plt.title("Traffic Volume Trend")
plt.xlabel("Index")
plt.ylabel("Traffic Volume")

plt.tight_layout()

plt.savefig("traffic_line.png")

plt.show()

print("\nTask 1 Completed")

# ==============================================
# TASK 2
# Custom Styled Chart
# ==============================================

avg = df.groupby("Congestion")["traffic_volume"].mean()

plt.figure(figsize=(6,4))

plt.bar(
    ["Low Traffic","High Traffic"],
    avg.values,
    color=["green","red"]
)

plt.title("Average Traffic Volume by Congestion")
plt.xlabel("Traffic Status")
plt.ylabel("Average Traffic Volume")

plt.axhline(
    avg.mean(),
    color="black",
    linestyle="--",
    label="Overall Mean"
)

plt.legend()

plt.tight_layout()

plt.savefig("custom_chart.png")

plt.show()

print("Task 2 Completed")

# ==============================================
# Features and Target
# ==============================================

X = df[[
    "traffic_volume",
    "avg_vehicle_speed",
    "vehicle_count_cars",
    "vehicle_count_trucks",
    "vehicle_count_bikes",
    "temperature",
    "humidity",
    "accident_reported"
]]

y = df["Congestion"]

# ==============================================
# TASK 3
# Train Test Split Explorer
# ==============================================

print("\n========== TASK 3 ==========")

best_accuracy = 0
best_split = 0

for split in [0.1,0.2,0.3]:

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=split,
        random_state=42
    )

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print("\nSplit :", split)
    print("Training Size :", len(X_train))
    print("Testing Size :", len(X_test))
    print("Accuracy :", round(accuracy,4))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_split = split

print("\nBest Split =", best_split)

# ==============================================
# TASK 4
# Logistic Regression Model
# ==============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=best_split,
    random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("\n========== TASK 4 ==========")

print(
    "Model Accuracy :",
    round(
        accuracy_score(y_test,prediction),
        4
    )
)

# Predict a New Traffic Sample

new_sample = pd.DataFrame([[
    820,     # traffic_volume
    28,      # avg_vehicle_speed
    550,     # vehicle_count_cars
    110,     # vehicle_count_trucks
    160,     # vehicle_count_bikes
    33,      # temperature
    72,      # humidity
    1        # accident_reported
]], columns=[
    "traffic_volume",
    "avg_vehicle_speed",
    "vehicle_count_cars",
    "vehicle_count_trucks",
    "vehicle_count_bikes",
    "temperature",
    "humidity",
    "accident_reported"
])

new_prediction = model.predict(new_sample)

print(
    "Prediction for New Traffic Sample =",
    new_prediction[0]
)

# ==============================================
# END OF PART 1
# ==============================================
# ==============================================
# TASK 5
# Feature Comparison
# ==============================================

print("\n========== TASK 5 ==========")

features = list(X.columns)

best_feature = ""
best_score = 0

for feature in features:

    X_single = df[[feature]]

    X_train_single, X_test_single, y_train_single, y_test_single = train_test_split(
        X_single,
        y,
        test_size=0.2,
        random_state=42
    )

    m = LogisticRegression(max_iter=1000)

    m.fit(X_train_single, y_train_single)

    pred = m.predict(X_test_single)

    score = accuracy_score(y_test_single, pred)

    print(feature, ":", round(score,4))

    if score > best_score:
        best_score = score
        best_feature = feature

print("\nBest Feature :", best_feature)

# ==============================================
# TASK 6
# Predicted vs Actual Plot
# ==============================================

print("\n========== TASK 6 ==========")

X_train_plot, X_test_plot, y_train_plot, y_test_plot = train_test_split(
    X,
    y,
    test_size=best_split,
    random_state=42
)

test_prediction = model.predict(X_test_plot)

plt.figure(figsize=(6,5))

plt.scatter(
    y_test_plot,
    test_prediction,
    color="blue"
)

plt.plot(
    [0,1],
    [0,1],
    color="red"
)

plt.xlabel("Actual Congestion")
plt.ylabel("Predicted Congestion")
plt.title("Traffic Congestion Prediction")

plt.tight_layout()

plt.savefig("prediction_plot.png")

plt.show()

print("Task 6 Completed")

# ==============================================
# TASK 7
# Save and Load Model
# ==============================================

pickle.dump(
    model,
    open("trafficiq_model.pkl","wb")
)

loaded_model = pickle.load(
    open("trafficiq_model.pkl","rb")
)

test_samples = [

    [700,32,480,80,120,30,60,0],

    [950,18,700,130,200,35,75,1],

    [450,55,300,40,80,27,55,0]

]

print("\n========== TASK 7 ==========")

for sample in test_samples:

    sample_df = pd.DataFrame(
        [sample],
        columns=[
            "traffic_volume",
            "avg_vehicle_speed",
            "vehicle_count_cars",
            "vehicle_count_trucks",
            "vehicle_count_bikes",
            "temperature",
            "humidity",
            "accident_reported"
        ]
    )

    result = loaded_model.predict(sample_df)

    print("Input :", sample)
    print("Prediction :", result[0])
    print()

print("TrafficIQ Model Saved Successfully")

# ==============================================
# TASK 8
# Mini Project Summary
# ==============================================

print("\n=================================")
print("PROJECT NAME")
print("TrafficIQ - Smart Traffic & Congestion Predictor")

print("\nDATASET")
print("smart_traffic_management_dataset.csv")

print("\nFEATURES")

for column in X.columns:
    print("-", column)

print("\nTARGET")
print("Congestion (0 = Low Traffic, 1 = High Traffic)")

print("\nPROJECT QUESTION")
print("Can Machine Learning Predict Traffic Congestion?")

print("\nALGORITHM")
print("Logistic Regression")

print("\nBEST TRAIN TEST SPLIT")
print(best_split)

print("\nMODEL ACCURACY")
print(round(accuracy_score(y_test, prediction),4))

print("\nBEST FEATURE")
print(best_feature)

print("=================================")

# ==============================================
# Visual Demo
# Confusion Matrix
# ==============================================

cm = confusion_matrix(
    y_test_plot,
    test_prediction
)

plt.figure(figsize=(5,5))

plt.imshow(
    cm,
    cmap="Blues"
)

plt.title("TrafficIQ Confusion Matrix")

plt.colorbar()

plt.xticks(
    [0,1],
    ["Low","High"]
)

plt.yticks(
    [0,1],
    ["Low","High"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(
            j,
            i,
            str(cm[i,j]),
            ha="center",
            va="center"
        )

plt.tight_layout()

plt.savefig("confusion_matrix.png")

plt.show()

# ==============================================
# Final Output
# ==============================================

print("\nGenerated Files")

print("- traffic_bar.png")
print("- traffic_scatter.png")
print("- traffic_histogram.png")
print("- traffic_line.png")
print("- custom_chart.png")
print("- prediction_plot.png")
print("- confusion_matrix.png")
print("- trafficiq_model.pkl")

print("\nProject Completed Successfully!")