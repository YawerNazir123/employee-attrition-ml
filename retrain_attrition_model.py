import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("Employee-Attrition.csv")

# Select ONLY deployment features
FEATURES = [
    "Age",
    "MonthlyIncome",
    "JobSatisfaction",
    "WorkLifeBalance",
    "TotalWorkingYears",
    "YearsAtCompany",
    "YearsWithCurrManager"
]

X = df[FEATURES]

# Encode target
y = df["Attrition"].map({"Yes": 1, "No": 0})

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# IMPORTANT CHECK
print("Number of features model expects:", model.n_features_in_)

# Save model
joblib.dump(model, "employee_attrition_prediction.pkl")

print("Model retrained and saved successfully")
