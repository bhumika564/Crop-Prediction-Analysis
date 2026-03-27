from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from joblib import load
from utils.preprocess import preprocess_data
import numpy as np
import time
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/', methods=['GET'])
def api():
    return jsonify({
        'status': 'success',
        'message': 'Crop Price Prediction API is running'
    })

@app.route('/api/model/xgboost/predict', methods=['POST'])
def predict_xgboost():
    try:
        # 1. Load Model and Metrics
        model = load('model/model_xgboost.pkl')
        with open('model/metrics_xgboost.json', 'r') as f:
            metrics = json.load(f)
        model_r2 = round(metrics.get('r2', 0), 4)

        # 2. Get Data and Preprocess
        data = request.get_json()
        df = pd.DataFrame([data])
        df = preprocess_data(df)

        # ✅ XGBOOST FIX: Isko 'weight' column training ke waqt mila tha
        if 'weight' not in df.columns:
            df['weight'] = 1
        
        # 3. Predict
        start_time = time.time()
        prediction = model.predict(df)[0]
        elapsed_time = round(time.time() - start_time, 4)

        return jsonify({
            'predicted_price': round(float(prediction), 2),
            'elapsed_time_sec': elapsed_time,
            'model_r2_score': model_r2
        })
    except Exception as e:
        print(f"XGBoost Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/model/randomforest/predict', methods=['POST'])
def predict_randomforest():
    try:
        # 1. Load Model and Metrics
        model = load('model/model_randomforest.pkl')
        with open('model/metrics_randomforest.json', 'r') as f:
            metrics = json.load(f)
        model_r2 = round(metrics.get('r2', 0), 4)

        # 2. Get Data and Preprocess
        data = request.get_json()
        df = pd.DataFrame([data])
        df = preprocess_data(df)

        # ✅ RANDOM FOREST FIX: Isko training ke waqt 'weight' nahi mila tha
        # Isliye agar preprocess_data ne weight add kiya hai, toh use hatao
        if 'weight' in df.columns:
            df = df.drop(columns=['weight'])

        # 3. Predict
        start_time = time.time()
        prediction = model.predict(df)[0]
        elapsed_time = round(time.time() - start_time, 4)

        return jsonify({
            'predicted_price': round(float(prediction), 2),
            'elapsed_time_sec': elapsed_time,
            'model_r2_score': model_r2
        })
    except Exception as e:
        print(f"Random Forest Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Docker ke liye host 0.0.0.0 hona zaroori hai
    app.run(debug=False, host='0.0.0.0', port=5000)