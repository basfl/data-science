import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("../../Simple Linear Regression/GPA_SAT/resources/gpa-sat.csv")

"""
our DV is gpa and our IV is sat
"""
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)

"""
here we are going to predict
given SAT=1844 what would be GPA
"""
y_pred_v = regressor.predict([[1844]])
print(f"predicted GPA for SAT=1844 is {y_pred_v}")
