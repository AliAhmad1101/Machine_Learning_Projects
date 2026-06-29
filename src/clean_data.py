import pandas as ps
import time

def inspect_data(df):
    print("\nMissing Values:\n")
    print(df.isnull().sum())
    time.sleep(1)
    print("\nDuplicate Values:\n")
    print(df.duplicated().sum())
    time.sleep(1)
    print("\nDataset Stats:\n")
    print(df.describe())
    time.sleep(1)
    print("\nDataset memory usage:\n")
    print(df.memory_usage())
    time.sleep(1)
    print("\nDataset Information:\n")
    print(df.info())
    time.sleep(1)
    print("\nData Inspected Successfully\n")

def clean_data(df):
    print("\nFilling Missing Values:\n")
    time.sleep(1)
    df["Marks"] = df["Marks"].fillna(df["Marks"].mean()).astype(int)
    print("\nValidating Study Hours, Attendance and Marks\n")
    time.sleep(1)
    df["Marks"] = df["Marks"].clip(lower=0, upper=100)
    df["Attendance"] = df["Attendance"].clip(lower=0, upper=100)
    df["StudyHours"] = df["StudyHours"].clip(lower=0, upper=24)
    df.to_csv("output/cleaned_data.csv", index=False)
    time.sleep(1)
    print("\nCleaned dataset saved successfully.\n")
    return df