# Titanic Survival Prediction

A beginner-friendly machine learning project that predicts whether a passenger would have survived the Titanic disaster based on a few passenger attributes. The project demonstrates the complete workflow of a basic classification model, from loading and preprocessing data to making predictions through a Flask web application.

---

## Features

* Load and inspect a CSV dataset
* Clean and preprocess data
* Encode categorical variables
* Train a Logistic Regression model
* Evaluate model performance
* Save the trained model using Joblib
* Predict survival through a web interface
* Run locally using Flask

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Flask
* HTML & CSS

---

## Project Structure

```text
Titanic-Survival-Prediction/
│
├── app.py
├── titanic_model.py
├── titanic_model.pkl
├── titanic_survival_beginner_500_rows.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## Dataset

The dataset contains 500 passenger records with the following columns:

* PassengerId
* Pclass
* Sex
* Age
* Fare
* Embarked
* Survived

The **Survived** column is the target variable:

* `0` → Did Not Survive
* `1` → Survived

---

## Workflow

1. Load the dataset.
2. Inspect the data using `head()`, `info()`, and `describe()`.
3. Handle missing values and duplicate records.
4. Encode categorical columns.
5. Split the dataset into training and testing sets.
6. Train a Logistic Regression model.
7. Evaluate the model using standard classification metrics.
8. Save the trained model.
9. Serve predictions through a Flask application.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Titanic-Survival-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Train the Model

```bash
python titanic_model.py
```

This generates the trained model file:

```text
titanic_model.pkl
```

### Start the Flask Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Input Parameters

The application accepts the following inputs:

| Feature         | Description                     |
| --------------- | ------------------------------- |
| Passenger Class | 1, 2 or 3                       |
| Gender          | Male or Female                  |
| Age             | Passenger age                   |
| Fare            | Ticket fare                     |
| Embarked        | Port of embarkation (C, Q or S) |

---

## Model

Algorithm used:

* Logistic Regression

Evaluation metrics:

* Accuracy
* Confusion Matrix
* Classification Report

---

## Future Improvements

* Compare multiple classification algorithms.
* Add feature scaling where appropriate.
* Display prediction confidence.
* Visualize dataset statistics on the web interface.
* Deploy the application to a cloud platform.

---

## License

This project is intended for educational purposes and personal learning.
