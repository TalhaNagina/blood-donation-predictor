# 📊 Final Report: Personalized Healthcare Recommendation System

## 🧠 Problem Statement

Predict whether a blood donor will donate again, and provide personalized healthcare recommendations based on user features like donation history.

---

## 📂 Dataset Overview

- Source: `blood.csv`
- Rows: ~748
- Features:
  - `Recency`: Months since last donation
  - `Frequency`: Total donations made
  - `Monetary`: Total volume donated (log-transformed)
  - `Time`: Months since first donation
  - `Class`: Target (1 = donated in March 2007, 0 = did not)

---

## 🔍 Exploratory Data Analysis

- Data had no nulls but outliers in `Monetary` (handled with `log1p`)
- Features like `Recency` and `Frequency` showed moderate correlation with `Class`
- Boxplots revealed skew in several features
- Distribution visualizations helped with scaling decisions

---

## 🔧 Preprocessing & Feature Engineering

- Applied `np.log1p` to `Monetary`
- Used `StandardScaler` for numeric features
- Split into train/test (80/20, stratified)
- Features used:
  - `Recency`, `Frequency`, `Monetary`, `Time`

---

## 🤖 Model Training

- Used Random Forest Classifier (`sklearn`)
- Accuracy: ~92%
- F1 Score: 0.91
- Saved using `joblib` for use in deployed app

---

## 🩺 Personalized Recommendations

- If prediction = 1 → “Regular check-up / Lifestyle guidance”
- If prediction = 0 → “No action needed”
- Built interactive Streamlit app with user input form + slider controls

---

## 🚀 Future Work

- Add more medical features (age, BMI, symptoms, etc.)
- Use XGBoost or LightGBM for performance boosting
- Add real medical labels for richer recommendations
- Deploy to Streamlit Cloud or Hugging Face Spaces

