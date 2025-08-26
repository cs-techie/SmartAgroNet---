import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import warnings
warnings.filterwarnings('ignore')
from PIL import Image

# Load and display header image
if os.path.exists("crop.png"):
    st.image("crop.png", use_column_width=True)

# Load dataset
df = pd.read_csv('Crop_recommendation.csv')
X = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# Train model
from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.3, random_state=42)
RF = RandomForestClassifier(n_estimators=20, random_state=5)
RF.fit(Xtrain,Ytrain)

# Save and load model
with open('RF.pkl', 'wb') as f:
    pickle.dump(RF, f)
RF_Model_pkl = pickle.load(open('RF.pkl','rb'))

# Prediction function
def predict_crop(n, p, k, temp, hum, ph, rain):
    return RF_Model_pkl.predict(np.array([n, p, k, temp, hum, ph, rain]).reshape(1, -1))[0]

# --- Streamlit UI ---
st.set_page_config(page_title="Smart Crop Recommendation", layout="wide")

# Custom CSS for modern dark theme
st.markdown("""
    <style>
    .main {background-color: #0f111a; color: #e0e6f0;}
    h1, h2, h3, h4 {color: #1de9b6;}
    .stButton>button {background-color: #1de9b6; color: #0f111a; font-weight: bold;}
    .stButton>button:hover {background-color: #14b38d; color: white;}
    .stNumberInput>div>input {background-color: #121524; color: #e0e6f0;}
    .stSidebar {background-color: #121524;}
    .stSidebar h2, .stSidebar h3 {color: #1de9b6;}
    </style>
""", unsafe_allow_html=True)

st.title("🌱 Smart Crop Recommendation System")
st.subheader("Enter the environmental details to get crop suggestions")

# Sidebar inputs
st.sidebar.header("Input Parameters")
nitrogen = st.sidebar.number_input("Nitrogen", 0.0, 140.0, 0.0, 0.1)
phosphorus = st.sidebar.number_input("Phosphorus", 0.0, 145.0, 0.0, 0.1)
potassium = st.sidebar.number_input("Potassium", 0.0, 205.0, 0.0, 0.1)
temperature = st.sidebar.number_input("Temperature (°C)", 0.0, 51.0, 25.0, 0.1)
humidity = st.sidebar.number_input("Humidity (%)", 0.0, 100.0, 50.0, 0.1)
ph = st.sidebar.number_input("pH Level", 0.0, 14.0, 6.5, 0.1)
rainfall = st.sidebar.number_input("Rainfall (mm)", 0.0, 500.0, 100.0, 0.1)

# Predict button
if st.sidebar.button("Predict"):
    inputs = [nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]
    if not any(inputs) or np.isnan(inputs).any():
        st.error("Please fill in all input fields with valid values before predicting.")
    else:
        crop = predict_crop(*inputs)
        st.success(f"🌾 The recommended crop is: **{crop}**")
        # Show crop image if available
        image_path = os.path.join('crop_images', crop.lower()+'.jpg')
        if os.path.exists(image_path):
            st.image(image_path, caption=crop, use_column_width=True)
        else:
            st.info("No image available for this crop.")
