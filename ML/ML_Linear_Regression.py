# Code by AmirMotefaker

# Machine Learning - Linear Regression
# The term regression is used when you try to find the relationship between variables.
# In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.

# # Solution 1 - Start by drawing a scatter plot
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()



# Solution 2 - Import scipy and draw the line of Linear Regression
import matplotlib.pyplot as plt
from scipy import stats

# Create the arrays that represent the values of the x and y axis
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Execute a method that returns some important key values of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(x, y)

# Create a function that uses the slope and intercept 
# values to return a new value. This new value represents 
# where on the y-axis the corresponding x value will be placed
def myfunc(x):
  return slope * x + intercept

# Run each value of the x array through the function. 
# This will result in a new array with new values for the y-axis:
mymodel = list(map(myfunc, x))

# Draw the original scatter plot:
plt.scatter(x, y)
# Draw the line of linear regression:
plt.plot(x, mymodel)
# Display the diagram:
plt.show()




# Solution 3 - R for Relationship
# How well does my data fit in a linear regression?
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)

# Output:
# -0.7585915243761551



# Solution 4 - Predict Future Values
# Predict the speed of a 10 years old car
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

speed = myfunc(10)

print(speed)

# Output:
# 85.59308314937454



# Solution 5 - Bad Fit?
# These values for the x- and y-axis should result in a very bad fit for linear regression
import matplotlib.pyplot as plt
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()



# Solution 6 - Bad Fit?
# You should get a very low r value.
import numpy
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)

# Output:
# 0.013318141542974908
