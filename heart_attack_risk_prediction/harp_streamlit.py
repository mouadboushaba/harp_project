import streamlit as st
from datetime import datetime
import requests
import pandas as pd


# Streamlit webpage layout
st.title('Heart Attack Risk Prediction')

# Creating input fields for user data

#Personal Information
age = st.number_input('Age', min_value=0, max_value=120, value=25)
sex = st.selectbox('Sex', ['Male', 'Female'])
country = st.text_input('Country', 'United States')

#Personal Health
cholesterol = st.number_input('Cholesterol', min_value=100, max_value=400, value=200)
blood_pressure = st.text_input('Blood Pressure (systolic/diastolic)', '120/80')
heart_rate = st.number_input('Heart Rate', min_value=40, max_value=200, value=70)
diabetes = st.selectbox('Diabetes', ['No', 'Yes'])
family_history = st.selectbox('Family History of Heart Disease', ['No', 'Yes'])
previous_heart_problems = st.selectbox('Previous Heart Problems', ['No', 'Yes'])
medication_use = st.selectbox('Medication Use', ['No', 'Yes'])
bmi = st.number_input('Body Mass Index (BMI)', min_value=10.0, max_value=40.0, value=22.0)
triglycerides = st.number_input('Triglycerides', min_value=50, max_value=400, value=150)

#Lifestyle
smoking = st.selectbox('Smoking', ['No', 'Yes'])
obesity = st.selectbox('Obesity', ['No', 'Yes'])
alcohol_consumption = st.selectbox('Alcohol Consumption', ['No', 'Yes'])
exercise_hours_per_week = st.number_input('Exercise Hours Per Week', min_value=0, max_value=40, value=3)
diet = st.selectbox('Diet Type', ['Healthy', 'Unhealthy'])
stress_level = st.slider('Stress Level', min_value=1, max_value=10, value=5)
sedentary_hours_per_day = st.number_input('Sedentary Hours Per Day', min_value=0, max_value=24, value=8)
income = st.selectbox('Income Level', ['Low', 'Medium', 'High'])
physical_activity_days_per_week = st.number_input('Physical Activity Days Per Week', min_value=0, max_value=7, value=3)
sleep_hours_per_day = st.number_input('Sleep Hours Per Day', min_value=0, max_value=24, value=7)

#URL to be placed
url = 'https://.../.../.../.../'

#Parms input
params = {
    'Age': age,
    'Sex': sex,
    'Cholesterol': cholesterol,
    'Blood_Pressure': blood_pressure,
    'Heart_Rate': heart_rate,
    'Diabetes': diabetes,
    'Family_History': family_history,
    'Smoking': smoking,
    'Obesity': obesity,
    'Alcohol_Consumption': alcohol_consumption,
    'Exercise_Hours_Per_Week': exercise_hours_per_week,
    'Diet': diet,
    'Previous_Heart_Problems': previous_heart_problems,
    'Medication_Use': medication_use,
    'Stress_Level': stress_level,
    'Sedentary_Hours_Per_Day': sedentary_hours_per_day,
    'Income': income,
    'BMI': bmi,
    'Triglycerides': triglycerides,
    'Physical_Activity_Days_Per_Week': physical_activity_days_per_week,
    'Sleep_Hours_Per_Day': sleep_hours_per_day,
    'Country': country
}

#Call Api
response = requests.get(url, params = params)
#result = round(float(response.json()["Heart Attack Risk"]), 2)

#Displaying prediction
st.subheader("Heart Attack Risk Estimation:")
st.write(f"${Heart Attack Risk}")

is_high_risk = prediction == 1

# Display the result in color
if is_high_risk:
    st.markdown(f'<h2 style="color: red;">High Risk of Heart Attack</h2>', unsafe_allow_html=True)
else:
    st.markdown(f'<h2 style="color: green;">Low Risk of Heart Attack</h2>', unsafe_allow_html=True)
