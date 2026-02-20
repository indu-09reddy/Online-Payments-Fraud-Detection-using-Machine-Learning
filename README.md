# Online-Payments-Fraud-Detection-using-Machine-Learning
Online Payments Fraud Detection using Machine Learning. This project builds a model to identify fraudulent and legitimate online transactions based on transaction details like amount and balance. It includes data preprocessing, model training, and performance evaluation to improve payment security.
Online Payments Fraud Detection Using Machine Learning
📌 Project Overview

This project aims to detect fraudulent online payment transactions using Machine Learning techniques. It analyzes historical transaction data, trains a predictive model, and integrates it into a Flask web application for real-time fraud detection.

The system is also prepared for IBM Cloud deployment.

🗂 Project Structure
online-payments-fraud-detection/
│
├── data/
│   └── PS_20174392719_1491204439457_logs.csv
│
├── flask/
│   ├── templates/
│   │   ├── home.html
│   │   ├── predict.html
│   │   └── submit.html
│   │
│   ├── app.py
│   ├── app_ibm.py
│   └── payments.pkl
│
├── training/
│   ├── ONLINE PAYMENTS FRAUD DETECTION.ipynb
│   └── payments.pkl
│
├── training_ibm/
│   └── online payments fraud prediction using ibm.ipynb
│
└── README.md
📁 Detailed Folder Explanation
🔹 Flask Application Structure

We are building a Flask application.

HTML pages are stored inside the templates folder.

app.py is the main Python script used for backend processing.

payments.pkl is the saved trained model.

This model is loaded inside Flask for real-time prediction.

🔹 Model File (payments.pkl)

payments.pkl is our saved Machine Learning model.

It is generated after training.

This model is used for Flask integration and prediction.

🔹 Training Folder

Contains model training notebook.

Includes data preprocessing, feature engineering, model building, and evaluation.

After training, the model is saved as payments.pkl.

🔹 Training_IBM Folder

Contains IBM Cloud deployment notebook.

Used to deploy the trained model on IBM Watson / IBM Cloud services.

🔹 Data Folder

Contains the dataset used for training and testing the fraud detection system.

⚙️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Flask

IBM Cloud

HTML

🚀 How the System Works

User enters transaction details in the web interface.

Flask app collects input data.

The saved model (payments.pkl) predicts whether the transaction is:

✅ Legitimate

❌ Fraudulent

Result is displayed on the web page.

📊 Model Information

Algorithm: Random Forest Classifier

Handles imbalanced dataset

Evaluation Metrics:

Precision

Recall

F1-Score

ROC-AUC

🎯 Key Features

✔ Real-time fraud detection
✔ Web-based interface
✔ IBM Cloud deployment ready
✔ Structured project organization
✔ Easy model integration
