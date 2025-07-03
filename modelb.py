# -----------------------------------------
# MODEL B: POLYNOMIAL REGRESSION (DEGREE 2)
# -----------------------------------------

# 📦 Import required libraries
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 🔹 Step 1: Load the dataset
housing = fetch_california_housing()
X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = housing.target

# 🔹 Step 2: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔹 Step 3: Create pipeline for Polynomial Regression (degree 2)
poly_pipeline = Pipeline([
    ("scaler", StandardScaler()),  # Standardize features
    ("poly_features", PolynomialFeatures(degree=2, include_bias=False)),
    ("lin_reg", LinearRegression())
])

# 🔹 Step 4: Fit the model
poly_pipeline.fit(X_train, y_train)

# 🔹 Step 5: Predict on test data
y_pred_poly = poly_pipeline.predict(X_test)

# 🔹 Step 6: Evaluate the model
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print("📊 Polynomial Regression (Degree 2) Results:")
print("➡️  R² Score :", round(r2_poly, 4))
print("➡️  Mean Squared Error (MSE):", round(mse_poly, 4))

# 🔹 Step 7: Visualize Actual vs Predicted
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred_poly, alpha=0.5, color='green')
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Polynomial Regression (Degree 2): Actual vs Predicted")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.tight_layout()
plt.show()
