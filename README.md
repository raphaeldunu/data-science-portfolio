# Data Science & Statistical Modeling Portfolio

## 🚀 Project Overview
This repository contains reproducible data analysis pipelines built in **R** and **Python**. It demonstrates end-to-end data processing, exploratory data analysis (EDA), feature engineering, correlation analysis, and Ordinary Least Squares (OLS) regression modeling.

---

## 📂 Repository Contents

### 1. `analysis.R` (R Programming Pipeline)
* **Dataset:** Uses the built-in `mtcars` dataset (motor trend vehicle performance metrics).
* **Key Steps:**
  * Structural inspection (`str()`) and summary statistics (`summary()`).
  * Feature engineering (`DispPerHP`: calculating engine displacement per horsepower).
  * Subset analysis (filtering manual transmission vehicles).
  * Correlation matrix computation across key performance variables.
  * Predictive OLS regression modeling (`lm(mpg ~ wt + hp)`) to predict fuel efficiency.
  * Automated diagnostic extraction of $R$-squared, adjusted $R$-squared, and F-statistics.

### 2. `analysis.py` (Python Data Science Pipeline)
* **Dataset:** Uses the `scikit-learn` California housing dataset.
* **Key Steps:**
  * Dataframe ingestion and inspection using `pandas` (`info()`, `describe()`).
  * Feature engineering (`RoomsPerHousehold`: deriving average rooms per household).
  * Correlation matrix analysis to evaluate linear relationships and multicollinearity.
  * Ordinary Least Squares (OLS) regression modeling using `statsmodels` to predict median house values.
  * Summary statistical evaluation of coefficients and model performance.

---

## 🛠️ Skills & Competencies Demonstrated
* **Languages:** R, Python
* **Libraries/Packages:** `pandas`, `numpy`, `statsmodels`, `scikit-learn`, base `stats`
* **Methodologies:** Exploratory Data Analysis (EDA), Data Cleaning & Integrity checks, Feature Engineering, OLS Regression Modeling, and Statistical Interpretation.
