import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# 🔁 Update this to your actual training dataset path
DATA_PATH = 'loan_dataset.csv'  # or whatever your CSV file is named

# 🔃 These are the categorical columns in your dataset
CATEGORICAL_COLUMNS = [
    'Gender',
    'Employment_Type',
    'Loan_Type',
    'Payment_History',
    'Collection_Method',
    'Legal_Action_Taken'
]

# 🔄 Load your training data
df = pd.read_csv(DATA_PATH)

label_encoders = {}

# 🔁 Fit LabelEncoders on each categorical column
for col in CATEGORICAL_COLUMNS:
    le = LabelEncoder()
    df[col] = df[col].fillna("Unknown")
    le.fit(df[col])
    label_encoders[col] = le
    print(f"{col} classes: {list(le.classes_)}")

# 💾 Save the encoders
joblib.dump(label_encoders, 'label_encoders.pkl')
print("\n✅ Label encoders re-trained and saved to 'label_encoders.pkl'")
