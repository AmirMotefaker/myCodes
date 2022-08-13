# Code by @AmirMotefaker

# Inverse Matrix

# # Solution 1 - NumPy
# # The inverse of a matrix is that matrix which when multiplied
# # with the original matrix will give as an identity matrix. 
# # The inverse of a matrix exists only if the matrix is non-singular i.e.,
# # determinant should not be 0. 
import numpy as np
  
A = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]])
  
print(np.linalg.inv(A))

# # Output:
# # [[ 0.17647059 -0.00326797 -0.02287582]
# #  [ 0.05882353 -0.13071895  0.08496732]
# #  [-0.11764706  0.1503268   0.05228758]]



# # Solution 2 - NumPy
import numpy as np
  
A = np.array([[6, 1, 1, 3],
              [4, -2, 5, 1],
              [2, 8, 7, 6],
              [3, 1, 9, 7]])
  
print(np.linalg.inv(A))

# # Output:
# # [[ 0.13368984  0.10695187  0.02139037 -0.09090909]
# #  [-0.00229183  0.02673797  0.14820474 -0.12987013]
# #  [-0.12987013  0.18181818  0.06493506 -0.02597403]
# #  [ 0.11000764 -0.28342246 -0.11382735  0.23376623]]



# Solution 3 - NumPy
import numpy as np
  
A = np.array([[[1., 2.], [3., 4.]],
              [[1, 3], [3, 5]]])
  
print(np.linalg.inv(A))

# Output:
# [[[-2.    1.  ]
#   [ 1.5  -0.5 ]]

#  [[-1.25  0.75]
#   [ 0.75 -0.25]]]
