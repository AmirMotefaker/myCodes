# Code by amotef@gmail.com

# Determinant Calculation

# A = [a b c 
#      d e f
#      g h i]

# => det(A) = aei + bfg + cdh - ceg - bdi - afh

import numpy as np
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])

print("Det of A: ", np.linalg.det(A))
