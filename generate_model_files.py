import joblib
import numpy as np
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# === Example model creation ===
X = [[30000, 3], [50000, 1], [10000, 2]]
y = [1, 0, 1]  # Dummy recovery status

# You can replace RandomForestClassifier with your actual model
model = RandomForestClassifier()
model.fit(X, y)

# === Label encoders for categorical columns ===
label_encoders = {
    'Gender': LabelEncoder().fit(['Male', 'Female']),
    'Employment_Type': LabelEncoder().fit(['Salaried', 'Self-employed']),
    'Loan_Type': LabelEncoder().fit(['Home', 'Personal', 'Auto']),
    'Collection_Method': LabelEncoder().fit(['Phone', 'Visit', 'Email']),
    # Add any more columns from your dataset that need encoding
}

# === Save to files ===
joblib.dump(model, 'model.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')

print("✅ model.pkl and label_encoders.pkl created successfully")
