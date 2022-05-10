# Code by amotef@gmail.com

# Determinant Calculation

# A = [a b c 
#      d e f
#      g h i]

# => det(A) = aei + bfg + cdh - ceg - bdi - afh

import time
start_time = time.time()   #Time at the start of program execution

import numpy as np
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

print("Det of A =", np.linalg.det(A))

end_time = time.time()   #Time at the end of execution
print ("Time of program execution:", (end_time - start_time))   # Time of program execution
