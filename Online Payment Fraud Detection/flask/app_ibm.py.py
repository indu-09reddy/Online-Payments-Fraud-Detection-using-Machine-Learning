from flask import Flask, render_template, request
import numpy as np
import requests
import json

app = Flask(__name__)

# ===============================
# IBM WATSON CREDENTIALS
# ===============================

API_KEY = "..."
DEPLOYMENT_URL = "..."

# Get IAM Token
def get_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "apikey": API_KEY,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict')
def predict():
    return render_template("predict.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":

        step = float(request.form['step'])
        type_t = float(request.form['type'])
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])
        oldbalanceDest = float(request.form['oldbalanceDest'])
        newbalanceDest = float(request.form['newbalanceDest'])

        input_data = [[step, type_t, amount,
                       oldbalanceOrg, newbalanceOrig,
                       oldbalanceDest, newbalanceDest]]

        token = get_token()

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }

        payload = {
            "input_data": [{
                "fields": ["step", "type", "amount",
                           "oldbalanceOrg", "newbalanceOrig",
                           "oldbalanceDest", "newbalanceDest"],
                "values": input_data
            }]
        }

        response = requests.post(
            DEPLOYMENT_URL,
            headers=headers,
            json=payload
        )

        prediction = response.json()

        # Extract prediction result
        result_value = prediction['predictions'][0]['values'][0][0]

        if result_value == 1:
            result = "⚠️ Fraudulent Transaction Detected!"
        else:
            result = "✅ Genuine Transaction"

        return render_template("submit.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
