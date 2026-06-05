import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #fff5f5 0%,
        #ffe6e6 50%,
        #ffd6d6 100%
    );
}

.main-title {
    text-align:center;
    color:#c1121f;
    font-size:55px;
    font-weight:800;
}

.sub-title {
    text-align:center;
    color:#555;
    font-size:20px;
    margin-bottom:30px;
}

.block-container {
    padding-top: 2rem;
}

.metric-box {
    background:white;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.15);
}

.stButton>button {
    width:100%;
    background:#c1121f;
    color:white;
    font-size:20px;
    font-weight:bold;
    border:none;
    border-radius:12px;
    padding:12px;
}

.stButton>button:hover {
    background:#780000;
    color:white;
}

.footer {
    text-align:center;
    color:#444;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD FILES
# -----------------------------
model = joblib.load("pkl_files/knn_heart_model.pkl")
scaler = joblib.load("pkl_files/heart_scaler.pkl")
expected_columns = joblib.load("pkl_files/heart_columns.pkl")

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.title("❤️ Heart Predictor")

    st.info("""
This ML application predicts
the likelihood of heart disease
using patient health data.

Developer:
**Alisha Rout**
""")

    st.success("Machine Learning Model: KNN")

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    "<h1 class='main-title'>❤️ Heart Disease Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>Enter your health details below to estimate your risk level.</p>",
    unsafe_allow_html=True
)

# -----------------------------
# INPUTS
# -----------------------------
col1, col2 = st.columns(2)

with col1:

    age = st.slider(
        "Age",
        18,
        100,
        40
    )

    sex = st.selectbox(
        "Sex",
        ["M", "F"]
    )

    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["ATA", "NAP", "TA", "ASY"]
    )

    resting_bp = st.number_input(
        "Resting Blood Pressure",
        80,
        250,
        120
    )

    cholesterol = st.number_input(
        "Cholesterol",
        100,
        600,
        200
    )

with col2:

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar > 120",
        [0, 1]
    )

    resting_ecg = st.selectbox(
        "Resting ECG",
        ["Normal", "ST", "LVH"]
    )

    max_hr = st.slider(
        "Maximum Heart Rate",
        60,
        220,
        150
    )

    exercise_angina = st.selectbox(
        "Exercise Induced Angina",
        ["Y", "N"]
    )

    oldpeak = st.slider(
        "Oldpeak",
        0.0,
        6.0,
        1.0
    )

    st_slope = st.selectbox(
        "ST Slope",
        ["Up", "Flat", "Down"]
    )

# -----------------------------
# HEALTH SUMMARY
# -----------------------------
st.markdown("## 📊 Health Summary")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Age",
        age
    )

with m2:
    st.metric(
        "Blood Pressure",
        resting_bp
    )

with m3:
    st.metric(
        "Cholesterol",
        cholesterol
    )

st.write("")

# -----------------------------
# PREDICT BUTTON
# -----------------------------
predict = st.button(
    "🔍 Predict Heart Disease Risk"
)

# -----------------------------
# PREDICTION
# -----------------------------
if predict:

    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)[0]

    st.markdown("---")

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error(
            "⚠️ High Risk of Heart Disease"
        )

        st.progress(85)

        st.warning("""
Please consult a healthcare professional
for further evaluation.
""")

    else:

        st.success(
            "✅ Low Risk of Heart Disease"
        )

        st.progress(25)

        st.info("""
Your current health indicators suggest
a lower risk level.
""")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")

st.markdown("""
<div class='footer'>
❤️ Built with Streamlit & Scikit-Learn<br>
Developed by Alisha Rout
</div>
""", unsafe_allow_html=True)
