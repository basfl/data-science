import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("../../Simple Linear Regression/GPA_SAT/resources/gpa-sat.csv")

"""
our DV is gpa and our IV is sat
"""
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Fitting Polynomial Regression to the dataset
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)



# Predicting a new result with Linear Regression
#print(lin_reg_2.predict(1844))
# Predicting a new result with Polynomial Regression
print(lin_reg_2.predict(poly_reg.fit_transform(1844)))

# Visualising the Polynomial Regression results
# following two lines are optional 
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, lin_reg_2.predict(
   poly_reg.fit_transform(X_grid)), color='blue')
plt.title('SAT vs GPA (SVR)')
plt.xlabel('SAT')
plt.ylabel('GPA')
plt.show()