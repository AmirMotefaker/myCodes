# Code by @AmirMotefaker

# Identity Matrix

# numpy.identity(n, dtype = None): 
# Return a identity matrix i.e. a square matrix with ones on the main diagonal.
import numpy as np
 
b = np.identity(2, dtype = float)
print("Matrix b : \n", b)
 
 
a = np.identity(4)
print("\nMatrix a : \n", a)

# Output:
# Matrix b : 
#  [[1. 0.]
#  [0. 1.]]

# Matrix a :
#  [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
