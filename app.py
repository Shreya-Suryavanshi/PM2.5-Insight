from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("pm25_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        pm25_value = float(request.form["pm25"])
        prediction = model.predict(np.array([[pm25_value]]))[0]

        # Mapping cluster → category
        cluster_labels = {
            0: "Good (0-50 µg/m³)",
            1: "Moderate (51-100 µg/m³)",
            2: "Unhealthy for Sensitive Groups (101-150 µg/m³)",
            3: "Unhealthy (151-200 µg/m³)",
            4: "Very Unhealthy (201-300 µg/m³)",
            5: "Hazardous (301+ µg/m³)"
        }

        result = cluster_labels.get(prediction, "Unknown Category")
        return render_template("home.html", result=f"Cluster: {prediction}, Category: {result}")

    except:
        return render_template("home.html", result="❌ Invalid Input. Please enter a number.")

if __name__ == "__main__":
    app.run(debug=True)
