# Code by AmirMotefaker

# Machine Learning - Multiple Regression

# # Solution 1 - Multiple Regression
import pandas
# We will use some methods from the sklearn module,
# so we will have to import that module as well
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']
# From the sklearn module we will use the LinearRegression()
# method to create a linear regression object.
regr = linear_model.LinearRegression()
# This object has a method called fit() that takes the independent
# and dependent values as parameters and fills the regression object
# with data that describes the relationship
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)

# Output:
# [107.2087328]



# # Solution 2 - Coefficient
import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)

# Output:
# [0.00755095 0.00780526]



# Solution 3 - Result Explained
import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)

# Output:
# [114.75968007]
