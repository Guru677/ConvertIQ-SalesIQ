import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv("dataset.csv")

# Encode categorical feature
df["device_type"] = df["device_type"].map({"mobile": 0, "desktop": 1})

# Encode target label
le = LabelEncoder()
df["dropoff_risk_encoded"] = le.fit_transform(df["dropoff_risk"])

X = df.drop(["dropoff_risk", "dropoff_risk_encoded"], axis=1)
y = df["dropoff_risk_encoded"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(le, open("label_encoder.pkl", "wb"))

print("Model trained and saved successfully!")
print("Train Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))
