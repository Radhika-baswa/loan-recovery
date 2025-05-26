from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load model and encoders
model = joblib.load('loan_recovery_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')
target_encoder = joblib.load('target_encoder.pkl')

# List of features expected from the user
FEATURE_COLUMNS = [
    'Age', 'Gender', 'Employment_Type', 'Monthly_Income',
    'Num_Dependents', 'Loan_Amount', 'Loan_Tenure', 'Interest_Rate',
    'Loan_Type', 'Collateral_Value', 'Outstanding_Loan_Amount',
    'Monthly_EMI', 'Payment_History', 'Num_Missed_Payments',
    'Days_Past_Due', 'Collection_Attempts', 'Collection_Method',
    'Legal_Action_Taken'
]
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Validate input
    if not all(key in data for key in FEATURE_COLUMNS):
        return jsonify({'error': 'Missing fields in input data'}), 400

    try:
        # Convert to DataFrame
        input_df = pd.DataFrame([data])

        # Encode categorical features
        for col, le in label_encoders.items():
            if col in input_df.columns:
                if data[col] not in le.classes_:
                    return jsonify({'error': f'Invalid value for {col}: {data[col]}'}), 400
                input_df[col] = le.transform([data[col]])

        # Predict
        prediction = model.predict(input_df)[0]
        prediction_label = target_encoder.inverse_transform([prediction])[0]

        # Add basic explanation (optional - simple rule-based logic)
        reason = ""
        if data['Payment_History'] == 'On Time':
            reason = "Borrower paid on time, showing good repayment behavior."
        elif data['Num_Missed_Payments'] > 3:
            reason = "Multiple missed payments reduce recovery chances."
        elif data['Legal_Action_Taken'] == 'Yes':
            reason = "Legal action was necessary due to high risk."
        else:
            reason = "Moderate risk, depends on further behavior."

        return jsonify({
            'prediction': prediction_label,
            'reason': reason
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500




# Run the app
if __name__ == '__main__':
    app.run(debug=True)

