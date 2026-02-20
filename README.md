Online Payments Fraud Detection using Machine Learning
📌 Project Description

This project focuses on detecting fraudulent online payment transactions using Machine Learning techniques. It analyzes transaction details such as amount, balance changes, and transaction type to predict whether a transaction is legitimate or fraudulent.

A Random Forest classifier is trained on historical transaction data and integrated into a Flask web application for real-time fraud prediction.

The goal of this project is to reduce financial loss, improve transaction security, and demonstrate the practical implementation of machine learning in fraud detection systems.

🚀 Key Highlights

Data preprocessing and feature engineering

Handling imbalanced datasets

Random Forest model training and evaluation

High accuracy fraud detection (~99%)

Flask-based web interface for real-time prediction

Model saved using pickle for deployment

🛠️ Technologies Used

Python

Pandas & NumPy

Scikit-learn

Flask

HTML

This project demonstrates how machine learning can be applied to real-world financial security problems in a simple and practical way.
▶️ How to Run

Train model:

python train_model.py

Move payments.pkl to flask folder

Run Flask app:

cd flask
python app.py


