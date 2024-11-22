# Credit Risk Analysis:
# This project focuses on creating an accurate model to predict credit risk, leveraging machine learning classifiers to assess the likelihood of borrowers defaulting on loans. The goal is to identify the best model for predicting credit defaults while also considering financial implications, such as profitability and risk management.

# Key Features:
# Data Preprocessing: Handling missing values, outliers, and scaling features to ensure high-quality input data for modeling.
# Model Selection: Evaluated multiple classifiers including Logistic Regression, Random Forest, XGBoost, and a Voting Classifier to identify the best-performing model.
# Evaluation Metrics: Utilized metrics such as Recall, Precision, F1 Score, AUC, and ROC Curve to assess model performance.
# Threshold Optimization: Explored the effect of different thresholds on model performance to balance false positives and false negatives, aiming for better financial decision-making.
# Financial Metrics: Focused on key metrics like Acceptance Rate and Bad Rate to quantify the financial impact of loan decisions.

# Key Findings:
# XGBoost outperformed other models in terms of Recall and F1 Score, making it the best choice for predicting credit defaults.
# Threshold selection is critical and has a significant impact on the model's ability to balance risk and profitability.
# Acceptance Rate and Bad Rate are valuable for understanding the financial implications of different thresholds, guiding better decision-making.
# Model Calibration and Feature Importance help ensure the model is both accurate and interpretable, improving its real-world application.

# Requirements:
# Python 3.12.1
# scikit-learn
# XGBoost
# pandas
# matplotlib
# seaborn
