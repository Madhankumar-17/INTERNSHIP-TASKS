# Student Performance Analysis using Pandas & NumPy

from pathlib import Path
import pandas as pd
import numpy as np

# Load Dataset
script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "student-mat.csv"
df = pd.read_csv(csv_path, sep=';')

print("=" * 60)
print("STUDENT PERFORMANCE ANALYSIS")
print("=" * 60)

# 1. Dataset Information
print("\nDataset Shape:", df.shape)
print("\nColumns:\n", list(df.columns))
print("\nFirst 5 Rows:\n", df.head())
print("\nLast 5 Rows:\n", df.tail())

# 2. Missing Values
print("\nMissing Values:\n", df.isnull().sum())

# Fill Missing Values
num_cols = df.select_dtypes(include=np.number).columns
obj_cols = df.select_dtypes(include='object').columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
df[obj_cols] = df[obj_cols].fillna("Unknown")

# 3. Data Types
print("\nData Types:\n", df.dtypes)

# 4. Basic Statistics
print("\nSummary Statistics:\n", df.describe())

# 5. Column Selection
print("\nAverage Age:", df["age"].mean())
print(df[["age", "studytime", "G3"]].head())

# 6. Hard Working Students
hard = df[df["studytime"] > 2]
print("\nHard Working Students:", len(hard))
print("Average Grade:", round(hard["G3"].mean(), 2))

# 7. Category Counts
print("\nGender Count:\n", df["sex"].value_counts())
print("\nInternet Count:\n", df["internet"].value_counts())

# 8. GroupBy Analysis
print("\nStudy Time vs Grade")
print(df.groupby("studytime")["G3"].mean())

print("\nGender vs Grade")
print(df.groupby("sex")["G3"].mean())

print("\nInternet vs Grade")
print(df.groupby("internet")["G3"].mean())

# 9. Absence Analysis
low = df[df["absences"] <= 3]["G3"].mean()
high = df[df["absences"] > 10]["G3"].mean()

print("\nAverage Grade (Low Absence):", round(low, 2))
print("Average Grade (High Absence):", round(high, 2))

# 10. Sorting
print("\nTop 5 Students")
print(df.sort_values("G3", ascending=False)[["school", "age", "G3"]].head())

# 11. Add New Columns
df["Average_Grade"] = (df["G1"] + df["G2"] + df["G3"]) / 3
df["Result"] = np.where(df["G3"] >= 10, "Pass", "Fail")

print("\nAverage Grade & Result")
print(df[["G1", "G2", "G3", "Average_Grade", "Result"]].head())

# 12. Correlation Matrix
print("\nCorrelation Matrix")
print(df[["age", "studytime", "absences", "G1", "G2", "G3"]].corr())

# 13. NumPy Marks Analysis
marks = np.array([78, 65, 89, 56, 92, 73, 81, 49, 68, 95])

print("\nNumPy Marks Analysis")
print("Marks:", marks)
print("Mean:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Standard Deviation:", round(np.std(marks), 2))
print("Passed Students:", len(marks[marks >= 50]))

# 14. Sample DataFrame Builder
students = pd.DataFrame({
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],
    "Age": [20, 21, 19, 22, 20],
    "City": ["Hyderabad", "Delhi", "Mumbai", "Chennai", "Pune"],
    "Marks": [85, 42, 73, 91, 56]
})

students["Result"] = np.where(students["Marks"] >= 50, "Pass", "Fail")

print("\nSample Student DataFrame")
print(students)

print("\nShape:", students.shape)
print("\nData Types:\n", students.dtypes)

print("\nProject Completed Successfully")