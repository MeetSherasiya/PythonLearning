import matplotlib as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()

# diabetes_X = diabetes.data[:, np.newaxis, 2]
diabetes_X = np.array([[1], [2], [3]])

diabetes_X_train = diabetes_X
diabetes_X_test = diabetes_X

diabetes_y_train = np.array([3, 2, 4])
diabetes_y_test = np.array([3, 2, 4])

model = linear_model.LinearRegression()

model.fit(diabetes_X_train, diabetes_y_train)

diabetes_y_predicted = model.predict(diabetes_X_test)

print("Mean squared error is: ", mean_squared_error(diabetes_y_test, diabetes_y_predicted))

print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)
