import pandas as ps
import time

def grading(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
    
def result(marks):
    if marks >= 60:
        return "Pass"
    else:
        return "Fail"

def transform(df):
    df["Grade"] = df["Marks"].apply(grading)
    df["Result"] = df["Marks"].apply(result)
    df["Performance Score"] = (df["Marks"] * 0.6 + df["Attendance"] * 0.3 + df["StudyHours"] * 0.1).round(2)
    df.to_csv("Output/cleaned_data.csv")
    toppers = df[df["Marks"] >= 90]
    failed = df[df["Marks"] < 60]
    toppers.to_csv("Output/toppers.csv")
    failed.to_csv("Output/failed_students.csv")
    time.sleep(1)
    print("\nToppers and Failed Students dataset saved successfully.")
    return df