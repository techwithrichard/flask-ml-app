from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model & scaler
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Get user inputs
            features = [
                float(request.form["OverallQual"]),
                float(request.form["GrLivArea"]),
                float(request.form["GarageCars"]),
                float(request.form["TotalBsmtSF"]),
                float(request.form["FullBath"]),
                float(request.form["YearBuilt"])
            ]
            
            # Preprocess input
            features_scaled = scaler.transform([features])
            
            # Predict house price
            prediction = model.predict(features_scaled)[0]

        except:
            prediction = "Invalid input. Please enter valid numbers."

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
