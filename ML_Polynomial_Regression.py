# Code by @AmirMotefaker

# Machine Learning - Polynomial Regression
# If your data points clearly will not fit a linear regression 
# (a straight line through all data points), it might be ideal 
# for polynomial regression.
# Polynomial regression, like linear regression, uses the 
# relationship between the variables x and y to find the best 
# way to draw a line through the data points.

# # Solution 1 - Polynomial Regression
# # Start by drawing a scatter plot
# import matplotlib.pyplot as plt

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# plt.scatter(x, y)
# plt.show()




# # Solution 2 - Import numpy and matplotlib then draw the line of Polynomial Regression
# import numpy
# import matplotlib.pyplot as plt

# # Create the arrays that represent the values of the x and y axis
# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# # NumPy has a method that lets us make a polynomial model
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# # Then specify how the line will display, we start at position 1, and end at position 22
# myline = numpy.linspace(1, 22, 100)

# # Draw the original scatter plot
# plt.scatter(x, y)
# # Draw the line of polynomial regression
# plt.plot(myline, mymodel(myline))
# # Display the diagram
# plt.show()



# # Solution 3 - R-Squared
# # How well does my data fit in a polynomial regression?
# import numpy
# from sklearn.metrics import r2_score

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# print(r2_score(y, mymodel(x)))

# # Output:
# 0.9432150416451026



# # Solution 4 - Predict Future Values
# # Predict the speed of a car passing at 17 P.M
# import numpy
# from sklearn.metrics import r2_score

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# speed = mymodel(17)
# print(speed)

# # Output:
# # 88.87331269698007



# # Solution 5 - Bad Fit?
# # These values for the x- and y-axis should result in a very bad fit for polynomial regression
# import numpy
# import matplotlib.pyplot as plt

# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# myline = numpy.linspace(2, 95, 100)

# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()



# Solution 6 - Bad Fit?
# And the r-squared value?
# You should get a very low r-squared value.
import numpy
from sklearn.metrics import r2_score

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

# Output:
# 0.009952707566680652
