# Code by AmirMotefaker

# Machine Learning - Percentiles
# Percentiles are used in statistics to give you a number 
# that describes the value that a given percent of the values are lower than.
# Example: Let's say we have an array of the ages of all the people that lives in a street.

# # Solution 1 
# # Use the NumPy percentile() method to find the percentiles
import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)

# # Output:
# # 43.0



# Solution 2
# What is the age that 90% of the people are younger than?
import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 90)

print(x)

# Output:
# 61.0
