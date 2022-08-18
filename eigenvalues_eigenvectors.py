# Code by @AmirMotefaker

# Eigenvalues and Eigenvectors

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


# Solution 1
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


# Output:
# Printing the Original square array:
#  [[5 1]
#  [4 2]]
# Printing the Eigen values of the given square array:
#  [6. 1.]
# Printing Right eigenvectors of the given square array:
#  [[ 0.70710678 -0.24253563]
#  [ 0.70710678  0.9701425 ]]



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
