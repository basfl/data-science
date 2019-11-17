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

# Visualising the SVR results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('SAT vs GPA (SVR)')
plt.xlabel('SAT')
plt.ylabel('GPA')
plt.show()


# Visualising the SVR results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.01) # choice of 0.01 instead of 0.1 step because the data is feature scaled
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('SAT vs GPA (SVR)')
plt.xlabel('SAT')
plt.ylabel('GPA')
plt.show()
