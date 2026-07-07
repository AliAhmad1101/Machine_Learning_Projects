from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("titanic_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    pclass = int(request.form["pclass"])
    gender = int(request.form["gender"])
    age = float(request.form["age"])
    fare = float(request.form["fare"])
    embarked = int(request.form["embarked"])

    prediction = model.predict([[pclass, gender, age, fare, embarked]])

    if prediction[0] == 1:
        result = "Passenger Will Survive"
    else:
        result = "Passenger Will Not Survive"

    return render_template("index.html", prediction=result)


if __name__ == "__main__":
    app.run(debug=True)