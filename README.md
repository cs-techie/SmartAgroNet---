<div align="center">
  <h1>🌱 SmartAgroNet: Smart Crop Recommendation & Plant Disease Identification</h1>
  <h3>🚀 AI-Powered Sustainable Farming Assistant</h3>
</div>

---

## 📖 Overview
**SmartAgroNet** is an innovative solution that uses **Machine Learning (ML)** and **Deep Learning (DL)** to help farmers improve productivity and make better decisions.  

The platform features:
- ✅ Smart Crop Recommendation using ML (based on soil nutrients, climate & rainfall)  
- ✅ Plant Disease Identification using CNN (deep learning image classifier)  
- ✅ Fertilizer Recommendation for soil & crop optimization  
- ✅ Real-time Weather Forecasting  
- ✅ Smart Farming Guide for planting & crop management  

Farmers can easily access all tools and insights via a **user-friendly web app**.

---

## 📑 Research Paper Reference  

This project is based on the following IEEE paper:

> **Title:** Smart Crop Recommendation System with Plant Disease Identification  
> **Authors:** P. Shankar, et al.  
> **Conference:** 2024 International Conference on Intelligent Sustainable Systems (ICISS)  
> **Publisher:** IEEE  
> **DOI:** [10.1109/ICISS.2024.10738975](https://doi.org/10.1109/ICISS.2024.10738975)  
> **IEEE Link:** [View IEEE Paper](https://ieeexplore.ieee.org/document/10738975)  
> **Full Paper (PDF):** [Download Here](IEEE_Paper.pdf)  

---

## 🚀 Features  

- 🌾 **Smart Crop Recommendation**  
  Leverages machine learning to suggest the most suitable crops based on soil nutrients, climate, and historical data.  

- 🩺 **Plant Disease Identification**  
  Uses **CNNs** to detect and classify plant diseases from leaf images for **early intervention**.  

- 🧪 **Fertilizer Recommendation**  
  Offers tailored fertilizer advice for different soil & crop needs.  

- 🌦 **Weather Forecasting**  
  Real-time temperature, humidity, and rainfall predictions for better planning.  

- 📘 **Smart Farming Guide**  
  Provides planting schedules & strategies to **maximize crop yield**.  

- 🖥 **User-Friendly Interface**  
  Built with **Streamlit** for interactive data entry and visual results.  

---

## 📊 Datasets  

### 📌 Crop Recommendation Dataset  
- **2200 rows** with soil and environmental factors: Nitrogen, Phosphorous, Potassium, pH, Temperature, Humidity, Rainfall  
- Used to predict the **most suitable crop**  
- Model tested with **7 classification algorithms**  

| Algorithm                | Accuracy (%) |
|--------------------------|--------------|
| Decision Tree            | 90.00        |
| Gaussian Naive Bayes     | 99.09        |
| Support Vector Machine   | 10.68        |
| Logistic Regression      | 95.23        |
| Random Forest            | **99.55** ✅ |
| XGBoost                  | 99.09        |
| KNN                      | 97.50        |

📌 **Best Model:** Random Forest (99.55% accuracy)  

---

### 📌 Plant Disease Identification Dataset  
- **70,295 training images** + **17,572 validation images**  
- Covers **38 diseases across 14 crops**  
- Images standardized to **128x128 resolution**  
- Dataset size: ~5 GB  

**Supported Crops (14):**  
`Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato`  

**Diseases Detected (38):**  
Includes Apple Scab, Black Rot, Tomato Blight, Powdery Mildew, Leaf Mold, Citrus Greening, etc.  

📌 **Best Model:** CNN trained with TensorFlow/Keras  

---

### 📌 Fertilizer Recommendation Dataset  
- Provides soil quality & crop-specific data  
- Generates **optimized fertilizer suggestions**  

---

## 🏗 Model Architectures  

### 🌾 Crop Recommendation Model  
- Algorithms: Decision Tree, GaussianNB, SVM, Logistic Regression, Random Forest, XGBoost, KNN  
- ✅ Random Forest achieved **99.55% accuracy**  

### 🩺 Plant Disease Identification Model  
- **CNN architecture** trained on plant leaf images  
- Covers **14 crops, 38 diseases**  
- High accuracy in **image classification**  

---

## 🖼 System Architecture  

```text
Farmer Input -> Preprocessing -> ML/DL Models -> Smart Recommendations
   |                |              |
   |                |              +-> Crop Suggestion
   |                |              +-> Disease Detection
   |                |              +-> Fertilizer Advice
   |                +-> Weather Forecasting
   +-> Web Interface (Streamlit)
