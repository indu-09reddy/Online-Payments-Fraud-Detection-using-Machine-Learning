Online Payments Fraud Detection Using Machine Learning
📌 Project Overview

This project aims to detect fraudulent online payment transactions using Machine Learning techniques. It analyzes historical transaction data, trains a predictive model, and integrates it into a Flask web application for real-time fraud detection.

The system is also prepared for IBM Cloud deployment.
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
⚙️ Technologies Used

Python

Pandas

NumPy

Scikit-learn

Flask

IBM Cloud

HTML

🚀 How the System
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
