# Code by @AmirMotefaker

# Eigenvalues and Eigenvector

# Eigen vector of a matrix A is a vector represented by a matrix X such that 
# when X is multiplied with matrix A, then the direction of the resultant matrix remains same as vector X.
# Mathematically, above statement can be represented as:
#           AX = λX
# where A is any arbitrary matrix, λ are eigen values and X is an eigen vector corresponding to each eigen value.

# Example:

# Suppose we have a matrix as: 
# [[1,2],
# [2,3]] 

# Eigenvalue we get from this matrix or square array is: 
# [-0.23606798 4.23606798]

# Eigenvectors of this matrix are: 
# [[-0.85065081 -0.52573111], 
# [ 0.52573111 -0.85065081]] 



# linalg.eig(a): Compute the eigenvalues and right eigenvectors of a square array.


# # Solution 1
import numpy as np
  
m = np.array([[5, 1],
              [4, 2]])
  
print("Printing the Original square array:\n",
      m)
  
w, v = np.linalg.eig(m)
  
print("Printing the Eigen values of the given square array:\n",
      w)
  
print("Printing Right eigenvectors of the given square array:\n",
      v)


# # Output:
# # Printing the Original square array:
# #  [[5 1]
# #  [4 2]]
# # Printing the Eigen values of the given square array:
# #  [6. 1.]
# # Printing Right eigenvectors of the given square array:
# #  [[ 0.70710678 -0.24253563]
# #  [ 0.70710678  0.9701425 ]]



# # Solution 2 
import numpy as np
  
m = np.array([[0, 2, 3],
              [2, 5, 4],
              [4, 2, 6]])
  
print("Printing the Original square array:\n",
      m)
  
w, v = np.linalg.eig(m)
  
print("Printing the Eigen values of the given square array:\n",
      w)
  
print("Printing Right eigenvectors of the given square array:\n",
      v)

# # Output:
# # Printing the Original square array:
# #  [[0 2 3]
# #  [2 5 4]
# #  [4 2 6]]
# # Printing the Eigen values of the given square array:
# #  [10.         -1.56155281  2.56155281]
# # Printing Right eigenvectors of the given square array:
# #  [[-0.33333333 -0.88174923 -0.03562293]
# #  [-0.66666667 -0.01857963 -0.84529398]
# #  [-0.66666667  0.47135241  0.53311265]]



# # Solution 3
import numpy as np
from numpy import linalg as LA

w, v = LA.eig(np.diag((1, 2, 3)))
print(w)
print(v)

# # Output:
# # [1. 2. 3.]
# # [[1. 0. 0.]
# #  [0. 1. 0.]
# #  [0. 0. 1.]]



# # Solution 4
import numpy as np
from numpy import linalg as LA

w, v = LA.eig(np.array([[1, -1], [1, 1]]))

print(w)
print(v)

# # Output:
# # [1.+1.j 1.-1.j]
# # [[0.70710678+0.j         0.70710678-0.j        ]
# #  [0.        -0.70710678j 0.        +0.70710678j]]



# # Solution 5
import numpy as np
from numpy import linalg as LA

a = np.array([[1, 1j], [-1j, 1]])

w, v = LA.eig(a)

print(w)
print(v)

# # Output:
# # [2.+0.j 0.+0.j]
# # [[ 0.        +0.70710678j  0.70710678+0.j        ]
# #  [ 0.70710678+0.j         -0.        +0.70710678j]]



# Solution 6
import numpy as np
from numpy import linalg as LA

a = np.array([[1 + 1e-9, 0], [0, 1 - 1e-9]])

w, v = LA.eig(a)

print(w)
print(v)

# Output:
# [1. 1.]
# [[1. 0.]
#  [0. 1.]]
