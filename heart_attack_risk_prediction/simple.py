from fastapi import FastAPI
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import joblib

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': True}


@app.get("/predict")
def predict(
        Age: int,
        Sex: str,
        Cholesterol  : int,
        Blood_Pressure :str,
        Heart_Rate   : int,
        Diabetes :int,
        Family_History: int,
        Smoking: int,
        Obesity : int,
        Alcohol_Consumption : int,
        Exercise_Hours_Per_Week : float,
        Diet : str,
        Previous_Heart_Problems : int,
        Medication_Use: int,
        Stress_Level: int,
        Sedentary_Hours_Per_Day: float,
        Income: int,
        BMI:float,
        Triglycerides : int,
        Physical_Activity_Days_Per_Week : int,
        Sleep_Hours_Per_Day : int,
        Country: str,
        Continent: str,
        Hemisphere: str
    ):
    """
    Make a single course prediction.
    Assumes `pickup_datetime` is provided as a string by the user in "%Y-%m-%d %H:%M:%S" format
    Assumes `pickup_datetime` implicitly refers to the "US/Eastern" timezone (as any user in New York City would naturally write)
    """
    data_dict = {
    'Age': [Age],
    'Sex': [Sex],
    'Cholesterol': [Cholesterol],
    'Blood Pressure': [Blood_Pressure],
    'Heart Rate': [Heart_Rate],
    'Diabetes': [Diabetes],
    'Family History': [Family_History],
    'Smoking': [Smoking],
    'Obesity': [Obesity],
    'Alcohol Consumption': [Alcohol_Consumption],
    'Exercise Hours Per Week': [Exercise_Hours_Per_Week],
    'Diet': [Diet],
    'Previous Heart Problems': [Previous_Heart_Problems],
    'Medication Use': [Medication_Use],
    'Stress Level': [Stress_Level],
    'Sedentary Hours Per Day': [Sedentary_Hours_Per_Day],
    'Income': [Income],
    'BMI': [BMI],
    'Triglycerides': [Triglycerides],
    'Physical Activity Days Per Week': [Physical_Activity_Days_Per_Week],
    'Sleep Hours Per Day': [Sleep_Hours_Per_Day],
    'Country': [Country],
    'Continent': [Continent],
    'Hemisphere': [Hemisphere]
    }

    X_pred = pd.DataFrame(data_dict, index=[0])


    model =pickle.load(open("/Users/mac/code/mouadboushaba/heart_attack_risk_prediction/model.pkl","rb"))
    assert model is not None

    label_encoder=joblib.load('models/label_encoder.joblib')
    scaler=joblib.load('models/scaler.joblib')


    object_columns = ["Sex", "Diet", "Country", "Continent", "Hemisphere"]
    for col in X_pred[object_columns]:
        X_pred[col] = label_encoder.transform(X_pred[col])

    X_pred[['Systolic Pressure', 'Diastolic Pressure']] = X_pred['Blood Pressure'].str.split('/', expand=True)
    X_pred.drop('Blood Pressure', axis=1, inplace=True)
    X_pred['Systolic Pressure'] = X_pred['Systolic Pressure'].astype(int)
    X_pred['Diastolic Pressure'] = X_pred['Diastolic Pressure'].astype(int)

    numerical_features = X_pred.select_dtypes(include=['int64', 'float64'])

    scaled_data = scaler.transform(numerical_features)
    X_processed = pd.DataFrame(scaled_data, columns=numerical_features.columns)

    y_pred = model.predict(X_processed)


    return {'ok': y_pred[0]}
