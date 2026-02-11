from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load('model.pkl')

@app.get('/predict')
def predict(median_income: float, ratio_habitantes_casa: float, longitude: float, latitude: float):
    features = np.array([[median_income, ratio_habitantes_casa, longitude, latitude]])
    prediction = model.predict(features)
    return {'precio_estimado': f'${prediction[0]:,.2f}'}