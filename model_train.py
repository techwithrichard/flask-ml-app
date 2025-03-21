import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("data/AmesHousing.csv")


# Standardize column names (remove spaces, make lowercase)
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()
print(df.columns.tolist())


# Standardized features (modify if needed)
features = ['overall_qual', 'gr_liv_area', 'garage_cars', 'total_bsmt_sf', 'full_bath', 'year_built']
target = 'saleprice'

# Ensure only existing features are selected
valid_features = [col for col in features if col in df.columns]
if not valid_features:
    raise KeyError("None of the selected features exist in the dataset. Check column names!")

X = df[valid_features]
y = df[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Save model & scaler
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model and scaler saved successfully.")
