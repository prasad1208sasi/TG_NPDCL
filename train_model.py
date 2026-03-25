sdimport numpy as np
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

# ===============================
# Load Data
# ===============================

data = pd.read_csv("cleaned_data.xls")
data = data.copy()

# ===============================
# Feature Engineering
# ===============================

data["Load_per_Service"] = data["Load"] / (data["TotServices"] + 1e-6)
data["Billing_Ratio"] = data["BilledServices"] / (data["TotServices"] + 1e-6)
data["Log_Load"] = np.log1p(data["Load"])

target = "Units"

X = data.drop(target, axis=1)
y = data[target]

# ===============================
# Train Test Split
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===============================
# Preprocessing
# ===============================

categorical_cols = ["Circle", "Division", "SubDivision", "Section"]
numerical_cols = [col for col in X.columns if col not in categorical_cols]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)

# ===============================
# Final Model with Best Params
# ===============================

final_model = RandomForestRegressor(
    n_estimators=334,
    max_depth=21,
    min_samples_split=7,
    min_samples_leaf=1,
    max_features="sqrt",
    random_state=42,
    n_jobs=-1
)

pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("model", final_model)
])

pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, "rf_units_model.pkl")

print("Model saved successfully ✅")
