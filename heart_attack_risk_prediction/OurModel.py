import pickle
import os
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import joblib



data = pd.read_csv('/Users/mac/code/mouadboushaba/heart_attack_risk_prediction/raw_data/heart_attack_prediction_dataset.csv')
data.drop("Patient ID", axis=1, inplace=True)

label_encoder = LabelEncoder()

object_columns = ["Sex", "Diet", "Country", "Continent", "Hemisphere"]
for col in data[object_columns]:
    data[col] = label_encoder.fit_transform(data[col])

data[['Systolic Pressure', 'Diastolic Pressure']] = data['Blood Pressure'].str.split('/', expand=True)

data.drop('Blood Pressure', axis=1, inplace=True)

data['Systolic Pressure'] = data['Systolic Pressure'].astype(int)
data['Diastolic Pressure'] = data['Diastolic Pressure'].astype(int)

numerical_features = data.select_dtypes(include=['int64', 'float64'])
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(numerical_features)
scaled_data_df = pd.DataFrame(scaled_data, columns=numerical_features.columns)

X = scaled_data_df.drop(columns=['Heart Attack Risk'])
y= scaled_data_df['Heart Attack Risk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

smote = SMOTE(random_state=43)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

model = DecisionTreeClassifier(criterion='gini',max_depth=5,min_samples_leaf=50,min_samples_split=2)
model.fit(X_resampled,y_resampled)

with open('/Users/mac/code/mouadboushaba/heart_attack_risk_prediction/model.pkl', 'wb') as file:
    pickle.dump(model, file)

joblib.dump(model,'harp_model.joblib')
joblib.dump(label_encoder, 'models/label_encoder.joblib')
joblib.dump(scaler, 'models/scaler.joblib')
#joblib.dump(tfidf_model, 'models/tf_idf_model.joblib')
#joblib.dump(tfidf_vectorizer, 'models/tfidf_vectorizer.joblib')
