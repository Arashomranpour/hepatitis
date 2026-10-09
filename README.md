<div align="center">

# 🩺 Hepatitis Mortality Prediction App

**An end-to-end ML project: data cleaning, EDA, feature selection, model building, interpretation with LIME and a Streamlit app with user login.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
![LIME](https://img.shields.io/badge/LIME-interpretability-informational)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)

</div>

---

## ✨ Overview

**Notebook (`i.ipynb`) - the full workflow**

`data prep → EDA → feature selection → build model → interpret model → serialization → Streamlit`

- 🧹 Missing values, outlier checks (boxplots, scatterplots, z-score, IQR).
- 📊 Feature importance and selection.
- 🤖 Models: **Decision Tree, Random Forest, Gradient Boosting, KNN, Logistic Regression**, ...
- 🔍 Model interpretation with **LIME**.
- 💾 Chosen models serialized with `joblib` (`dt_model.pkl`, `gb_model.pkl`).

**Streamlit app (`st.py`) - "Disease mortality Prediction App"**

- 🔐 **Sign up / Login** backed by SQLite (`mydatabase.py`) with hashed passwords.
- 📈 **Plot** - explore the cleaned dataset and pick features to visualise.
- 🎯 **Prediction** - fill in the patient's values, choose Decision Tree / Gradient Boost / Random Forest and get the mortality prediction.

> ⚠️ Educational project - not for clinical use.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/hepatitis.git
cd hepatitis
pip install pandas numpy scikit-learn seaborn matplotlib lime joblib streamlit jupyter
streamlit run st.py
```

## 📁 Project Structure

```
.
├── i.ipynb                       # Full analysis & modelling notebook
├── st.py                         # Streamlit app
├── mydatabase.py                 # SQLite user table helpers
├── hepatitis.data  cleaned.csv   # Data
├── dt_model.pkl  gb_model.pkl    # Trained models
└── costs/                        # Dataset cost files
```

## 🛠️ Tech Stack

`scikit-learn` · `LIME` · `pandas` · `Seaborn` · `Streamlit` · `SQLite`
