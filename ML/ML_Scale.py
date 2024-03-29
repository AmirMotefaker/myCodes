# Code by @AmirMotefaker

# Machine Learning - Scale

# # Solution 1
# # Scale all values in the Weight and Volume columns:
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

# print(scaledX)

# # Output:
# # [[-2.10389253 -1.59336644]
# #  [-0.55407235 -1.07190106]
# #  [-1.52166278 -1.59336644]
# #  [-1.78973979 -1.85409913]
# #  [-0.63784641 -0.28970299]
# #  [-1.52166278 -1.59336644]
# #  [-0.76769621 -0.55043568]
# #  [ 0.3046118  -0.28970299]
# #  [-0.7551301  -0.28970299]
# #  [-0.59595938 -0.0289703 ]
# #  [-1.30803892 -1.33263375]
# #  [-1.26615189 -0.81116837]
# #  [-0.7551301  -1.59336644]
# #  [-0.16871166 -0.0289703 ]
# #  [ 0.14125238 -0.0289703 ]
# #  [ 0.15800719 -0.0289703 ]
# #  [ 0.3046118  -0.0289703 ]
# #  [-0.05142797  1.53542584]
# #  [-0.72580918 -0.0289703 ]
# #  [ 0.14962979  1.01396046]
# #  [ 1.2219378  -0.0289703 ]
# #  [ 0.5685001   1.01396046]
# #  [ 0.3046118   1.27469315]
# #  [ 0.51404696 -0.0289703 ]
# #  [ 0.51404696  1.01396046]
# #  [ 0.72348212 -0.28970299]
# #  [ 0.8281997   1.01396046]
# #  [ 1.81254495  1.01396046]
# #  [ 0.96642691 -0.0289703 ]
# #  [ 1.72877089  1.01396046]
# #  [ 1.30990057  1.27469315]
# #  [ 1.90050772  1.01396046]
# #  [-0.23991961 -0.0289703 ]
# #  [ 0.40932938 -0.0289703 ]
# #  [ 0.47215993 -0.0289703 ]
# #  [ 0.4302729   2.31762392]]




# Solution 2 - Predict CO2 Values
# Predict the CO2 emission from a 1.3 liter car that weighs 2300 kilograms
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("cars2.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)

# Output:
# [107.2087328]
