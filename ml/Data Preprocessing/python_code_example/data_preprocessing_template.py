from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("./resources/Data.csv")
X = dataset.iloc[:, :-1].values  # Get all the columns expect the last one
Y = dataset.iloc[:, 3].values  # Get the last column
"""
handleing missing data by adding mean value
in this case columns 1&2 have missing data
"""
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
# print(X)

"""
handling the catagory of data
in this case country cloumn and purchased column
basically we do not want text 
in terms of the country does not make sense to simply
have number ,we add dummy variable meaning we change the 
country to corresonding three column so there is
no order between them
"""
labelecnoder_x = LabelEncoder()
X[:, 0] = labelecnoder_x.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
# Encoding the Dependent Variable
labelencoder_y = LabelEncoder()
Y = labelencoder_y.fit_transform(Y)
# print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0)
# print(X_train)

"""
we need to scale our data,
ML uses the euclidean distance , there range for salary is considerable 
bigger than age, therefore it dominate and cause issue for ML
"""
# feature scaling
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
