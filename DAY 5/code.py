# ===============================
# SMART TRAFFIC MANAGEMENT SYSTEM
# ===============================
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# --------------------------------
# Function 1 : Load Dataset
# --------------------------------
def load_dataset():
    file = os.path.join(os.path.dirname(__file__),
                        "smart_traffic_management_dataset.csv")
    df = pd.read_csv(file)
    print("\nDataset Loaded Successfully!")
    return df
    print("\nDataset Loaded Successfully!")
    return df


# --------------------------------
# Function 2 : Display Dataset
# --------------------------------
def display_dataset(df):
    print("\nFirst 5 Rows")
    print(df.head())

    print("\nLast 5 Rows")
    print(df.tail())


# --------------------------------
# Function 3 : Dataset Information
# --------------------------------
def dataset_info(df):
    print("\nDataset Shape :", df.shape)

    print("\nColumns")
    print(df.columns)

    print("\nData Types")
    print(df.dtypes)


# --------------------------------
# Function 4 : Missing Values
# --------------------------------
def missing_values(df):
    print("\nMissing Values")
    print(df.isnull().sum())


# --------------------------------
# Function 5 : Statistical Summary
# --------------------------------
def statistics(df):
    print("\nStatistical Summary")
    print(df.describe(include='all'))


# --------------------------------
# Function 6 : Data Cleaning
# --------------------------------
def clean_data(df):

    # Fill numeric columns
    num_cols = df.select_dtypes(include=np.number).columns

    for col in num_cols:
        df[col].fillna(df[col].mean(), inplace=True)

    # Fill categorical columns
    cat_cols = df.select_dtypes(include='object').columns

    for col in cat_cols:
        df[col].fillna("Unknown", inplace=True)

    print("\nData Cleaned Successfully")

    return df


# --------------------------------
# Function 7 : Encode Columns
# --------------------------------
def encode_columns(df):

    encoder = LabelEncoder()

    for col in df.select_dtypes(include='object').columns:
        df[col] = encoder.fit_transform(df[col])

    print("\nCategorical Columns Encoded")

    return df


# --------------------------------
# Function 8 : Correlation
# --------------------------------
def correlation(df):

    print("\nCorrelation Matrix")

    corr = df.corr()

    print(corr)

    plt.figure(figsize=(10,8))
    sns.heatmap(corr,
                annot=True,
                cmap='coolwarm')

    plt.title("Correlation Heatmap")
    plt.savefig("heatmap.png")
    plt.show()


# --------------------------------
# Function 9 : Charts
# --------------------------------
def charts(df):

    plt.figure(figsize=(8,5))
    df['traffic_volume'].hist()
    plt.title("Traffic Volume Distribution")
    plt.savefig("traffic_volume.png")
    plt.show()


    plt.figure(figsize=(8,5))
    sns.countplot(x='signal_status', data=df)
    plt.title("Signal Status")
    plt.savefig("signal_status.png")
    plt.show()


    plt.figure(figsize=(8,5))
    plt.scatter(df['traffic_volume'],
                df['avg_vehicle_speed'])

    plt.xlabel("Traffic Volume")
    plt.ylabel("Average Speed")
    plt.title("Traffic vs Speed")
    plt.savefig("traffic_speed.png")
    plt.show()


# --------------------------------
# Function 10 : Train Model
# --------------------------------
def train_model(df):

    X = df.drop("signal_status", axis=1)

    y = df["signal_status"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print("\nAccuracy :", accuracy)

    print("\nClassification Report")
    print(classification_report(y_test, prediction))

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, prediction))

    return model


# --------------------------------
# Function 11 : Save Model
# --------------------------------
def save_model(model):

    pickle.dump(model,
                open("model.pkl", "wb"))

    print("\nModel Saved Successfully")


# --------------------------------
# Function 12 : Predict 3 Cases
# --------------------------------
def predict_cases(model, df):

    sample = df.drop("signal_status", axis=1).head(3)

    prediction = model.predict(sample)

    print("\nPrediction for First 3 Records")

    for i in range(3):
        print("Case", i+1, ":", prediction[i])


# --------------------------------
# Main Function
# --------------------------------
def main():

    file = "smart_traffic_management_dataset.csv"

    df = load_dataset()

    display_dataset(df)

    dataset_info(df)

    missing_values(df)

    statistics(df)

    df = clean_data(df)

    df = encode_columns(df)

    correlation(df)

    charts(df)

    model = train_model(df)

    save_model(model)

    predict_cases(model, df)

    print("\nProject Completed Successfully")


# --------------------------------
# Run Program
# --------------------------------
if __name__ == "__main__":
    main()