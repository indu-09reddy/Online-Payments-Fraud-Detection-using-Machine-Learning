from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("payments.pkl", "rb"))

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

        features = np.array([[step, type_t, amount,
                              oldbalanceOrg, newbalanceOrig,
                              oldbalanceDest, newbalanceDest]])

        prediction = model.predict(features)

        if prediction[0] == 1:
            result = "⚠️ Fraudulent Transaction Detected!"
        else:
            result = "✅ Genuine Transaction"

        return render_template("submit.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
