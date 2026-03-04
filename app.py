import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰",
    layout="wide"
)

# Load model
model = joblib.load("insurance_model.pkl")

# Title Section
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>
    💰 Medical Insurance Cost Prediction
    </h1>
    <p style='text-align: center; font-size:18px;'>
    Predict insurance charges using Machine Learning
    </p>
    """,
    unsafe_allow_html=True
)

st.write("---")

# Sidebar Inputs
st.sidebar.header("Enter Patient Details")

age = st.sidebar.slider("Age", 18, 100, 30)

sex = st.sidebar.selectbox(
    "Gender",
    ["male", "female"]
)

bmi = st.sidebar.slider(
    "BMI",
    10.0,
    50.0,
    25.0
)

children = st.sidebar.slider(
    "Number of Children",
    0,
    5,
    0
)

smoker = st.sidebar.selectbox(
    "Smoker",
    ["yes", "no"]
)

region = st.sidebar.selectbox(
    "Region",
    ["southwest", "southeast", "northwest", "northeast"]
)

# Create DataFrame
input_data = pd.DataFrame({
    "age":[age],
    "sex":[sex],
    "bmi":[bmi],
    "children":[children],
    "smoker":[smoker],
    "region":[region]
})

# Layout columns
col1, col2 = st.columns(2)

# Show input data
with col1:
    st.subheader("📋 Input Data")
    st.dataframe(input_data)

# Visualization
with col2:
    st.subheader("📊 BMI Visualization")

    fig, ax = plt.subplots()

    ax.bar(["Your BMI"], [bmi])

    ax.set_ylabel("BMI Value")

    st.pyplot(fig)

st.write("---")

# Prediction Button
if st.button("Predict Insurance Cost 💰"):

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
        <div style="background-color:#D5F5E3;padding:25px;border-radius:10px">
        <h2 style="color:#145A32;text-align:center">
        Estimated Insurance Cost: ${prediction:,.2f}
        </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()

st.write("---")

st.markdown(
"""
### 📊 About This App

This application predicts **medical insurance charges** based on patient data.

The model uses **Random Forest Regression** with preprocessing pipeline.

Features used:

- Age
- Gender
- BMI
- Number of Children
- Smoking Status
- Region

Built using:

- Python
- Scikit-Learn
- Streamlit
"""
)
