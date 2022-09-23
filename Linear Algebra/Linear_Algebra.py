# Code by @AmirMotefaker

# Linear Algebra

# Solution 1
import numpy as np
 
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
 
# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
 
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
 
# Determinant of a matrix
print("\nDeterminant of A:", np.linalg.det(A))
 
# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))
 
print("\nMatrix A raised to power 3:\n",
           np.linalg.matrix_power(A, 3))

# Output:
# Rank of A: 3

# Trace of A: 11

# Determinant of A: -306.0

# Inverse of A:
#  [[ 0.17647059 -0.00326797 -0.02287582]
#  [ 0.05882353 -0.13071895  0.08496732]
#  [-0.11764706  0.1503268   0.05228758]]

# Matrix A raised to power 3:
#  [[336 162 228]
#  [406 162 469]
#  [698 702 905]]
