import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('diabetes.csv')

# Chart 1
plt.figure(figsize=(6,4))
df['Outcome'].value_counts().plot(kind='bar')
plt.title('Diabetes Distribution')
plt.xlabel('Outcome')
plt.ylabel('Count')
plt.savefig('chart1.png')
plt.close()

# Chart 2
plt.figure(figsize=(6,4))
plt.hist(df['Glucose'], bins=20)
plt.title('Glucose Distribution')
plt.xlabel('Glucose')
plt.ylabel('Frequency')
plt.savefig('chart2.png')
plt.close()

# Chart 3
plt.figure(figsize=(6,4))
plt.scatter(df['Age'], df['BMI'])
plt.title('Age vs BMI')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.savefig('chart3.png')
plt.close()

print("Charts saved successfully.")
import pickle

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Enter Patient Details")

glucose = float(input("Glucose: "))
blood_pressure = float(input("Blood Pressure: "))
bmi = float(input("BMI: "))
age = float(input("Age: "))

prediction = model.predict(
    [[glucose, blood_pressure, bmi, age]]
)

if prediction[0] == 1:
    print("\nPrediction: Diabetic")
else:
    print("\nPrediction: Not Diabetic")
    import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv('diabetes.csv')

print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

# Features
X = df[
    [
        'Glucose',
        'BloodPressure',
        'BMI',
        'Age'
    ]
]

# Target
y = df['Outcome']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

# Save Model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")