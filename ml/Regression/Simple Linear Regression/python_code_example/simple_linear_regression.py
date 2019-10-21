import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv("./resources/Salary_Data.csv")

X = dataset.iloc[:, :-1].values  # first column which is experience and IV
y = dataset.iloc[:, 1].values  # last column which is salary and our DV

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1/3, random_state=0)

# Fitting Simple Linear Regression to the Training set
regressor = LinearRegression()
# This will calculate the b0 and b1 coeffients
regressor.fit(X_train, y_train)

"""
 Predicting the Test set results
 We use X_test which is test data for years of experience
 base on that we get salary prediction so we can compare
 y_test with y_pred in other word
 y_test contains real salaries while
 y_pred contains the prediction salaries base on the model
"""
y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()