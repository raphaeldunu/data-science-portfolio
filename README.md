# ==============================================================================
# Project: Exploratory Data Analysis and Linear Regression Modeling
# Description: Demonstrates data cleaning, summary statistics, correlation 
#              analysis, and OLS regression modeling in R.
# ==============================================================================

# 1. Load Required Libraries (using built-in datasets for portability)
library(stats)
library(utils)

# 2. Data Inspection & Preparation
# Using the built-in 'mtcars' dataset as a clean, standard demonstration set
data("mtcars")

# View the structure and summary of the dataset
cat("--- Dataset Structure ---\n")
str(mtcars)

cat("\n--- Summary Statistics ---\n")
print(summary(mtcars))

# 3. Data Transformation & Custom Feature Engineering
# Create a new efficiency metric: displacement per horsepower
mtcars$DispPerHP <- mtcars$disp / mtcars$hp

# Filter observations: isolate cars with manual transmission (am == 1)
manual_cars <- subset(mtcars, am == 1)
cat("\nNumber of manual transmission cars analyzed:", nrow(manual_cars), "\n")

# 4. Statistical Analysis & Correlation
# Compute correlation matrix for numeric performance metrics
performance_vars <- mtcars[, c("mpg", "hp", "wt", "qsec")]
cor_matrix <- cor(performance_vars)

cat("\n--- Correlation Matrix ---\n")
print(round(cor_matrix, 2))

# 5. Predictive Modeling (Ordinary Least Squares Regression)
# Model miles per gallon (mpg) against weight (wt) and horsepower (hp)
regression_model <- lm(mpg ~ wt + hp, data = mtcars)

cat("\n--- Regression Model Summary ---\n")
print(summary(regression_model))

# 6. Automated Model Diagnostic Output Generation
diagnostics <- data.frame(
  Metric = c("R-Squared", "Adjusted R-Squared", "F-Statistic"),
  Value = c(
    summary(regression_model)$r.squared,
    summary(regression_model)$adj.r.squared,
    summary(regression_model)$fstatistic[1]
  )
)

cat("\n--- Model Diagnostics Summary ---\n")
print(diagnostics)
# data-science-portfolio
Exploratory data analysis and OLS regression modelling in R and Python
