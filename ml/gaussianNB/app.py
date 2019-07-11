from sklearn.naive_bayes import GaussianNB
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
clf = GaussianNB()
clf.fit(X, Y)
# GaussianNB()
print(clf.predict([[-0.8, -1]]))
accuracy_rate = clf.score(X, Y, sample_weight=None)
print(f'rate of accuracy is {accuracy_rate}')
