import streamlit as st
import numpy as np
import pandas as pd
import pickle


with open('scaler.pkl', 'rb') as f:
    loaded_scaler = pickle.load(f)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


st.title("Agricultural Crop Price Prediction")


st.header("Enter the crop details to predict price")

day = st.selectbox('Select a day', list(range(1, 32)))
month = st.selectbox('Select a month', list(range(1, 13)))
crop = st.selectbox('Crop Name', ['Ragi', 'Rice', 'Onion', 'Coconut', 'Tomato'])  # Example crops
district = st.selectbox('District', ['ba','ch','my','tu','ha'])  # Example districts

# Convert 'day' and 'month' to cyclic features
day_sin = np.sin(2 * np.pi * day / 31)
day_cos = np.cos(2 * np.pi * day / 31)
month_sin = np.sin(2 * np.pi * month / 12)
month_cos = np.cos(2 * np.pi * month / 12)





input_data = pd.DataFrame({
    'day_sin': [day_sin],
    'day_cos': [day_cos],
    'month_sin': [month_sin],
    'month_cos': [month_cos],
    'District Name_Chamrajnagar': [1 if district == 'ch' else 0],
    'District Name_Hassan': [1 if district == 'ha' else 0],
    'District Name_Mysore': [1 if district == 'my' else 0],
    'District Name_Tumkur': [1 if district == 'tu' else 0],
    'Commodity_Onion': [1 if crop == 'Onion' else 0],
    'Commodity_Ragi (Finger Millet)': [1 if crop == 'Ragi' else 0],
    'Commodity_Rice': [1 if crop == 'Rice' else 0],
    'Commodity_Tomato': [1 if crop == 'Tomato' else 0]

})

ip= loaded_scaler.transform(input_data)


if st.button('Predict Price'):
    # Make prediction using the trained model
    predicted_price = model.predict(ip)
    
    # Display the predicted price
    st.write(f"The predicted price for the selected crop is: ₹ {predicted_price[0]:.2f}")
