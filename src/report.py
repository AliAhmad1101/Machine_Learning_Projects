import pandas as ps
import time

def create_report(df):
    total = len(df)
    passs = len(df[df["Result"] == "Pass"])
    fail = len(df[df["Result"] == "Fail"])
    highest = df["Marks"].max()
    lowest = df["Marks"].min()
    average = df["Marks"].mean()
    attends = df["Attendance"].mean()
    grade = df["Grade"].value_counts()
    time.sleep(1)
    print("\nGrade Distribution:")
    print(grade)


    report = {
        "Total Students" : total,
        "Passed Students" : passs,
        "Failed Students" : fail,
        "Highest Marks" : highest,
        "Lowest Marks" : lowest,
        "Average Marks" : average,
        "Average Attendance" : attends,
    }
    time.sleep(1)
    print("\nThe Final Reports and Datasets are Ready...")
    report_df = ps.DataFrame(report.items(), columns=["Metric", "Value"])
    report_df.to_csv("Output/report.csv", index=False)