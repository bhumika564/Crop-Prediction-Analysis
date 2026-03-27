# 🌾 CropXpert - Crop Price Prediction System

**CropXpert** is an end-to-end Machine Learning application designed to predict crop prices based on environmental and market factors such as Rainfall, Region, MSP, and demand. The goal is to empower farmers and stakeholders with accurate, data-driven financial insights.

---

## 🌐 Go to Website
Click here to access the live application: **[CropXpert Live](https://crop-prediction-analysis-8rxh-pycjmh0qb.vercel.app)**

---

## 🚀 Project Deployment Links
- **Frontend URL:** [https://crop-prediction-analysis-8rxh-pycjmh0qb.vercel.app](https://crop-prediction-analysis-8rxh-pycjmh0qb.vercel.app)
- **Backend API:** [https://crop-prediction-analysis-application.onrender.com](https://crop-prediction-analysis-application.onrender.com)

## ✨ Key Features
- **Dual Model Selection:** Users can choose between **XGBoost** and **Random Forest** models for prediction.
- **Real-time Analytics:** Displays the predicted price along with the model's **R² Score** and processing time.
- **Interactive Dashboard:** A modern, fast, and responsive UI built with React (Vite).
- **Dynamic Data Processing:** Handles multiple variables including transport costs, storage availability, and government schemes.

## 🛠️ Tech Stack
- **Frontend:** React.js (Vite), CSS3, JavaScript (ES6+)
- **Backend:** Flask (Python), Flask-CORS
- **Machine Learning:** Scikit-learn, XGBoost, Pandas, Joblib
- **Deployment:** Vercel (Frontend), Render (Backend)

## 📖 How it Works
1. **Input:** The user fills out the dashboard form with crop-specific details.
2. **API Communication:** The React frontend sends a POST request containing the data to the Flask API hosted on Render.
3. **ML Inference:** The backend preprocesses the data and loads the trained `.pkl` models to generate a prediction.
4. **Visualization:** The results (Predicted Price and Accuracy metrics) are sent back and rendered on the user's dashboard.