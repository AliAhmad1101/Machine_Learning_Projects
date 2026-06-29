# Student Performance Data Handling and Analysis System

## Overview

This project is developed using **Python** and the **Pandas** library to perform basic data handling and analysis on a student dataset. The project reads student data from a CSV file, cleans the data, performs analysis, and generates reports.

The purpose of this project is to understand how Pandas can be used for real-world data processing tasks such as data cleaning, filtering, grouping, statistical analysis, and report generation.

---

## Features

The project includes the following functionalities:

* Load student data from a CSV file.
* Display dataset information and summary.
* Check for missing values and duplicate records.
* Clean and validate the dataset.
* Generate new columns such as Grade, Result, and Performance Score.
* Filter students based on different conditions.
* Perform statistical analysis.
* Sort and group student records.
* Generate a final report.
* Export processed data into CSV files.

---

## Project Structure

```
Student_Data_Project/
│
├── data/
│   └── student_dataset_v2.csv
│
├── output/
│   ├── cleaned_data.csv
│   ├── toppers.csv
│   ├── failed_students.csv
│   ├── low_attendance.csv
│   ├── high_study_hours.csv
│   └── report.csv
│
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── transform.py
│   ├── analyze.py
│   └── report.py
│
├── main.py
└── README.md
```

---

## Modules

### 1. Data Loading

* Reads the CSV file.
* Displays first and last five records.
* Shows dataset shape, column names, and data types.

### 2. Data Inspection

* Checks missing values.
* Finds duplicate records.
* Displays summary statistics.
* Shows memory usage and dataset information.

### 3. Data Cleaning

* Removes duplicate rows.
* Handles missing values.
* Validates marks, attendance, and study hours.
* Saves the cleaned dataset.

### 4. Data Transformation

* Creates Grade column.
* Creates Result column.
* Calculates Performance Score.

### 5. Data Filtering

Creates separate CSV files for:

* Top-performing students
* Failed students
* Students with attendance below 75%
* Students studying more than 8 hours

### 6. Data Analysis

Calculates:

* Average Marks
* Highest Marks
* Lowest Marks
* Average Attendance
* Average Study Hours
* Pass Percentage
* Fail Percentage
* Grade Distribution

### 7. Sorting

Sorts students by:

* Marks
* Attendance
* Study Hours

### 8. Grouping

Uses `groupby()` to calculate:

* Average marks by grade
* Number of students in each grade
* Average attendance by grade

### 9. Statistical Analysis

Calculates:

* Mean
* Median
* Mode
* Standard Deviation
* Variance
* Correlation Matrix

### 10. Report Generation

Generates a final report containing:

* Total Students
* Passed Students
* Failed Students
* Highest Marks
* Lowest Marks
* Average Marks
* Average Attendance
* Grade-wise Distribution

---

## Requirements

Install Pandas before running the project.

```bash
pip install pandas
```

---

## How to Run

1. Place the dataset inside the **data** folder.
2. Open the project in your Python IDE or VS Code.
3. Run:

```bash
python main.py
```

The generated CSV files will be saved inside the **output** folder.

---

## Output Files

The project generates the following files:

* cleaned_data.csv
* toppers.csv
* failed_students.csv
* report.csv

---

## Technologies Used

* Python 3
* Pandas
* CSV Files

---

## Learning Outcomes

After completing this project, I learned how to:

* Read and write CSV files using Pandas.
* Clean and preprocess datasets.
* Create new columns using existing data.
* Filter and sort records.
* Perform statistical analysis.
* Use `groupby()` for data aggregation.
* Generate reports from processed data.
* Organize a Python project into multiple modules.

---

## Author

**Ali Ahmad Khan**

Course: B.Tech
Branch: CSE-AI
Year: 3rd
