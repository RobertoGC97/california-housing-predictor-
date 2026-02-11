import streamlit as st
import joblib
import numpy as np

model = joblib.load('model.pkl')

st.title('🏠 California Housing Predictor')
st.write('Predice el precio de una vivienda en California')

median_income = st.slider('Ingreso mediano', 0.0, 15.0, 3.0)
ratio_habitantes_casa = st.slider('Habitantes por casa', 1.0, 10.0, 3.0)
longitude = st.slider('Longitud', -124.0, -114.0, -119.0)
latitude = st.slider('Latitud', 32.0, 42.0, 37.0)

if st.button('Predecir'):
    features = np.array([[median_income, ratio_habitantes_casa, longitude, latitude]])
    prediction = model.predict(features)
    st.success(f'Precio estimado: ${prediction[0]:,.2f}')