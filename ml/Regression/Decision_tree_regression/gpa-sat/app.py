import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("../../Simple Linear Regression/GPA_SAT/resources/gpa-sat.csv")

"""
our DV is gpa and our IV is sat
"""
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)

"""
here we are going to predict
given SAT=1844 what would be GPA
"""
y_pred_v = regressor.predict([[1844]])
print(f"predicted GPA for SAT=1844 is {y_pred_v}")

# Visualising the Decision Tree Regression results (higher resolution)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()