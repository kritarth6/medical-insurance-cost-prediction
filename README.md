# 💰 Insurance Cost Prediction App

This project predicts **medical insurance charges** using Machine Learning.

The model is trained using the **Insurance Dataset from Kaggle** and deployed with **Streamlit Cloud**.

---

## 🚀 Live Demo
(After deployment paste your Streamlit link here)

---

## 📊 Dataset

Dataset used:
https://www.kaggle.com/datasets/mirichoi0218/insurance

Features in dataset:

- age
- sex
- bmi
- children
- smoker
- region
- charges (target)

---

## 🧠 Machine Learning Model

Model used:

Random Forest Regressor

Pipeline includes:

- StandardScaler for numeric features
- OneHotEncoder for categorical features

---

## ⚙️ Tech Stack

- Python
- Pandas
- Scikit-Learn
- Streamlit
- Joblib

---

## 📂 Project Structure
insurance-cost-prediction
│
├── app.py
├── insurance_model.pkl
├── requirements.txt
└── README.md


---

## 📈 How It Works

1. User enters insurance details.
2. Data is passed into the trained ML pipeline.
3. Model predicts estimated insurance charges.

---

## 🖥️ Run Locally

Install dependencies


pip install -r requirements.txt


Run the app


streamlit run app.py


---

## 📌 Author

Kritarth Joshi



