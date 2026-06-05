❤️ Heart Disease Risk Prediction using Machine Learning

An end-to-end Machine Learning system that analyzes patient clinical data to predict the likelihood of heart disease. The project covers the complete ML lifecycle including data preprocessing, exploratory data analysis, model building, evaluation, and deployment as an interactive web application.

🚀 Live Demo

👉 Try the deployed application here:
https://heart-disease-eda-ml-dh7vah2lgmvkhaykzdbdm7.streamlit.app/

📌 Project Summary

Cardiovascular diseases remain one of the leading causes of death globally. Early detection using machine learning can assist in identifying high-risk individuals and supporting preventive healthcare decisions.

This project builds a predictive classification system that estimates whether a patient is at risk of heart disease based on key medical attributes.

The workflow follows a complete end-to-end data science pipeline used in real-world ML applications.

⚙️ ML Pipeline Overview
Data Collection & Understanding
Data Cleaning & Preprocessing
Exploratory Data Analysis (EDA)
Feature Engineering
Feature Scaling & Encoding
Model Training & Comparison
Performance Evaluation
Model Selection & Deployment
📂 Project Structure
heart-disease-eda-ml/
│
├── data/
│   └── heart.csv
│
├── images/
│   ├── correlation_heatmap.png
│   ├── target_distribution.png
│   └── model_results.png
│
├── notebooks/
│   └── heart_final.ipynb
│
├── app.py                      # Streamlit web application
├── knn_heart_model.pkl        # Trained ML model (deployment artifact)
├── requirements.txt
├── README.md
└── .gitignore
📊 Dataset Description

The dataset contains clinical parameters used for predicting heart disease risk.

Feature	Description
Age	Age of the patient
Sex	Gender
ChestPainType	Type of chest pain
RestingBP	Resting blood pressure
Cholesterol	Serum cholesterol level
FastingBS	Fasting blood sugar
RestingECG	ECG results at rest
MaxHR	Maximum heart rate achieved
ExerciseAngina	Exercise-induced angina
Oldpeak	ST depression induced by exercise
ST_Slope	Slope of peak exercise ST segment
HeartDisease	Target variable
🎯 Target Definition
0 → No Heart Disease
1 → Heart Disease Present
🧠 Machine Learning Models

The following classification models were implemented and compared:

Logistic Regression (Baseline + Interpretable)
Decision Tree Classifier
Random Forest Classifier (Best Performing)
📈 Model Evaluation

Models were evaluated using standard classification metrics:

Accuracy Score
Precision
Recall
F1 Score
Confusion Matrix
🏆 Key Insight:

Ensemble-based models (Random Forest) performed better due to their ability to handle non-linear relationships in medical data.

📊 Exploratory Data Analysis (EDA)

Key analyses performed:

Missing Value Analysis
Duplicate Detection
Statistical Summary
Correlation Analysis
Feature Distribution Analysis
Outlier Detection
Target Class Balance Analysis
📌 Visual Insights

Correlation Heatmap


Target Distribution


🧹 Data Preprocessing

The following preprocessing techniques were applied:

Handling missing values
Encoding categorical variables
Feature scaling using StandardScaler
Train-test splitting
🌐 Web Application (Deployment)

The trained model is deployed as an interactive web application using Streamlit.

Features of the App:
Real-time prediction of heart disease risk
User-friendly medical input form
Instant classification output
Probability-based risk estimation
Deployment Workflow:
Code pushed to GitHub
Connected to Streamlit Cloud
Configured app.py as entry point
Installed dependencies via requirements.txt
Successfully deployed as a live application
🚀 How to Run Locally
1. Clone the Repository
git clone https://github.com/AlishaRout-art/heart-disease-eda-ml.git
cd heart-disease-eda-ml
2. Install Dependencies
pip install -r requirements.txt
3. Run Jupyter Notebook
jupyter notebook

Open:

notebooks/heart_final.ipynb
💻 Run Web App Locally
streamlit run app.py
🔮 Future Enhancements
Hyperparameter tuning using GridSearchCV
Cross-validation for robust evaluation
SHAP-based explainability (feature impact visualization)
Add prediction history tracking
Deploy backend API using FastAPI
Integrate database for storing predictions
🎯 Key Learnings

This project helped me gain hands-on experience in:

End-to-end Machine Learning workflow design
Data preprocessing and feature engineering
Model selection and evaluation strategies
Real-world dataset handling
Web deployment using Streamlit
GitHub project structuring for portfolio readiness
👨‍💻 Author

Alisha Rout
B.Tech Computer Science Engineering

Interests:
Machine Learning 🤖
Data Science 📊
Software Development 💻
