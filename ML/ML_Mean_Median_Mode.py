# Code by @AmirMotefaker

# Machine Learning - Mean Median Mode

# # Solution 1 - Mean
# # Use the NumPy mean() method to find the average speed
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)

print(x)

# # Output:
# # 89.76923076923077



# # Solution 2 - Median
# # Use the NumPy median() method to find the middle value
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)

# # Output:
# # 87.0



# # Solution 3 - Median -Using the NumPy module
import numpy

speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print(x)

# # Output:
# # 86.5



# Solution 3 - The Mode value is the value that appears the most number of times
# Use the SciPy mode() method to find the number that appears the most
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)

# Output:
# ModeResult(mode=array([86]), count=array([3]))
