# Code by @AmirMotefaker

# Machine Learning - Categorical Data

# # Solution 1 - Categorical Data
import pandas as pd

cars = pd.read_csv('data.csv')
print(cars.to_string())

# # Output:
# #          Car       Model  Volume  Weight  CO2  Unnamed: 5
# # 0       Toyota        Aygo    1000     790   99         NaN
# # 1   Mitsubishi  Space Star    1200    1160   95         NaN
# # 2        Skoda      Citigo    1000     929   95         NaN
# # 3         Fiat         500     900     865   90         NaN
# # 4         Mini      Cooper    1500    1140  105         NaN
# # 5           VW         Up!    1000     929  105         NaN
# # 6        Skoda       Fabia    1400    1109   90         NaN
# # 7     Mercedes     A-Class    1500    1365   92         NaN
# # 8         Ford      Fiesta    1500    1112   98         NaN
# # 9         Audi          A1    1600    1150   99         NaN
# # 10     Hyundai         I20    1100     980   99         NaN
# # 11      Suzuki       Swift    1300     990  101         NaN
# # 12        Ford      Fiesta    1000    1112   99         NaN
# # 13       Honda       Civic    1600    1252   94         NaN
# # 14      Hundai         I30    1600    1326   97         NaN
# # 15        Opel       Astra    1600    1330   97         NaN
# # 16         BMW           1    1600    1365   99         NaN
# # 17       Mazda           3    2200    1280  104         NaN
# # 18       Skoda       Rapid    1600    1119  104         NaN
# # 19        Ford       Focus    2000    1328  105         NaN
# # 20        Ford      Mondeo    1600    1584   94         NaN
# # 21        Opel    Insignia    2000    1428   99         NaN
# # 22    Mercedes     C-Class    2100    1365   99         NaN
# # 23       Skoda     Octavia    1600    1415   99         NaN
# # 24       Volvo         S60    2000    1415   99         NaN
# # 25    Mercedes         CLA    1500    1465  102         NaN
# # 26        Audi          A4    2000    1490  104         NaN
# # 27        Audi          A6    2000    1725  114         NaN
# # 28       Volvo         V70    1600    1523  109         NaN
# # 29         BMW           5    2000    1705  114         NaN
# # 30    Mercedes     E-Class    2100    1605  115         NaN
# # 31       Volvo        XC70    2000    1746  117         NaN
# # 32        Ford       B-Max    1600    1235  104         NaN
# # 33         BMW           2    1600    1390  108         NaN
# # 34        Opel      Zafira    1600    1405  109         NaN
# # 35    Mercedes         SLK    2500    1395  120         NaN



# # Solution 2 - One Hot Encoding
# One Hot Encode the Car column:
import pandas as pd

cars = pd.read_csv('data.csv')
ohe_cars = pd.get_dummies(cars[['Car']])

print(ohe_cars.to_string())

# # Output:
# #    Car_Audi  Car_BMW  Car_Fiat  Car_Ford  Car_Honda  Car_Hundai  Car_Hyundai  Car_Mazda  Car_Mercedes  Car_Mini  Car_Mitsubishi  Car_Opel  Car_Skoda  Car_Suzuki  Car_Toyota  Car_VW  Car_Volvo
# # 0          0        0         0         0          0           0            0          0             0         0               0         0          0           0           1       0          0
# # 1          0        0         0         0          0           0            0          0             0         0               1         0          0           0           0       0          0
# # 2          0        0         0         0          0           0            0          0             0         0               0         0          1           0           0       0          0
# # 3          0        0         1         0          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 4          0        0         0         0          0           0            0          0             0         1               0         0          0           0           0       0          0
# # 5          0        0         0         0          0           0            0          0             0         0               0         0          0           0           0       1          0
# # 6          0        0         0         0          0           0            0          0             0         0               0         0          1           0           0       0          0
# # 7          0        0         0         0          0           0            0          0             1         0               0         0          0           0           0       0          0
# # 8          0        0         0         1          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 9          1        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 10         0        0         0         0          0           0            1          0             0         0               0         0          0           0           0       0          0
# # 11         0        0         0         0          0           0            0          0             0         0               0         0          0           1           0       0          0
# # 12         0        0         0         1          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 13         0        0         0         0          1           0            0          0             0         0               0         0          0           0           0       0          0
# # 14         0        0         0         0          0           1            0          0             0         0               0         0          0           0           0       0          0
# # 15         0        0         0         0          0           0            0          0             0         0               0         1          0           0           0       0          0
# # 16         0        1         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 17         0        0         0         0          0           0            0          1             0         0               0         0          0           0           0       0          0
# # 18         0        0         0         0          0           0            0          0             0         0               0         0          1           0           0       0          0
# # 19         0        0         0         1          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 20         0        0         0         1          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 21         0        0         0         0          0           0            0          0             0         0               0         1          0           0           0       0          0
# # 22         0        0         0         0          0           0            0          0             1         0               0         0          0           0           0       0          0
# # 23         0        0         0         0          0           0            0          0             0         0               0         0          1           0           0       0          0
# # 24         0        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          1
# # 25         0        0         0         0          0           0            0          0             1         0               0         0          0           0           0       0          0
# # 26         1        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 27         1        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 28         0        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          1
# # 29         0        1         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 30         0        0         0         0          0           0            0          0             1         0               0         0          0           0           0       0          0
# # 31         0        0         0         0          0           0            0          0             0         0               0         0          0           0           0       0          1
# # 32         0        0         0         1          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 33         0        1         0         0          0           0            0          0             0         0               0         0          0           0           0       0          0
# # 34         0        0         0         0          0           0            0          0             0         0               0         1          0           0           0       0          0
# # 35         0        0         0         0          0           0            0          0             1         0               0         0          0           0           0       0          0



# # Solution 3 - Predict CO2
import pandas
from sklearn import linear_model

# The pandas module allows us to read csv files and manipulate DataFrame objects:
cars = pandas.read_csv("data.csv")
# It also allows us to create the dummy variables:
ohe_cars = pandas.get_dummies(cars[['Car']])

# select the independent variables (X) and add the dummy variables columnwise
X = pandas.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']

# fit the data to a linear regression
regr = linear_model.LinearRegression()
regr.fit(X,y)

##predict the CO2 emission of a Volvo where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])

print(predictedCO2)

# # Output:
# # [122.45153299]



# # Solution 4 - Dummifying
import pandas as pd

colors = pd.DataFrame({'color': ['blue', 'red']})

print(colors)

# # Output:
# #   color
# # 0  blue
# # 1   red



# # Solution 5 - Dummifying
import pandas as pd

colors = pd.DataFrame({'color': ['blue', 'red']})
dummies = pd.get_dummies(colors, drop_first=True)

print(dummies)

# # Output:
# #   color_red
# # 0          0
# # 1          1



# Solution 6 - Dummifying
import pandas as pd

colors = pd.DataFrame({'color': ['blue', 'red', 'green']})
dummies = pd.get_dummies(colors, drop_first=True)
dummies['color'] = colors['color']

print(dummies)

# Output:
#    color_green  color_red  color
# 0            0          0   blue
# 1            0          1    red
# 2            1          0  green
