# ==============================================================================
# Project: Exploratory Data Analysis & OLS Regression in Python
# Description: Demonstrates dataframe manipulation, statistical summaries, 
#              feature engineering, and Ordinary Least Squares (OLS) regression.
# ==============================================================================

import pandas as pd
import numpy as np
import statsmodels.api as sm

# 1. Load Sample Data
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing(as_frame=True)
df = housing.frame.head(500) # Sample subset for clean presentation

# 2. Data Inspection
print("--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics ---")
print(df.describe())

# 3. Feature Engineering
# Create custom ratio: average rooms per household
df['RoomsPerHousehold'] = df['AveRooms'] / df['AveOccup']

# 4. Correlation Analysis
# Isolate key metrics to evaluate linear relationships
corr_matrix = df[['MedHouseVal', 'MedInc', 'HouseAge', 'RoomsPerHousehold']].corr()
print("\n--- Correlation Matrix ---")
print(corr_matrix.round(2))

# 5. Ordinary Least Squares (OLS) Regression Modeling
# Target: Median House Value (MedHouseVal)
# Predictors: Median Income, House Age, Rooms Per Household
X = df[['MedInc', 'HouseAge', 'RoomsPerHousehold']]
y = df['MedHouseVal']

# Add constant for the intercept term
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()

print("\n--- Regression Results Summary ---")
print(model.summary())
