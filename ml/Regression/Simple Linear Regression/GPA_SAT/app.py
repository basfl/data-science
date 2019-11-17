from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("./resources/gpa-sat.csv")

"""
our DV is gpa and our IV is sat
"""
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1/3, random_state=0)

# Fitting Simple Linear Regression to the Training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)
"""
here we are going to predict
given SAT=1844 what would be GPA
"""
y_pred_v = regressor.predict([[1844]])
print(f"predicted GPA for SAT=1844 is {y_pred_v}")

y_pred = regressor.predict(X_test)


# Visualising the Training set results
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('SAT vs GPA (Training set)')
plt.xlabel('SAT')
plt.ylabel('GPA')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title('SAT vs GPA (Test set)')
plt.xlabel('SAT')
plt.ylabel('GPA')
plt.show()
