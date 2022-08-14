# Code by @AmirMotefaker

# Scalars, Vectors, Matrices & Tensors


# Scalars
# Scalars: A scalar is a single number
# For example: n



# Vectors
# Vectors: A vector is an array of numbers arranged in some order, 
# as opposed to the single numbered scalar.

# # Defining a vector in Python
import numpy as np
v = np.array([2, 4, 6])
print(v)
 
# # Output:
# # [2 4 6]


# # Indexing a vector
import numpy as np

x = np.linspace(-np.pi, np.pi, 10)
print(x)
# # [-3.14159265 -2.44346095 -1.74532925 -1.04719755 -0.34906585  0.34906585
# #   1.04719755  1.74532925  2.44346095  3.14159265]
print (x[1:4])
# # [-2.44346095 -1.74532925 -1.04719755]
print (x[0:-1:2])
# # [-3.14159265 -1.74532925 -0.34906585  1.04719755  2.44346095]
print (x[:])
# # [-3.14159265 -2.44346095 -1.74532925 -1.04719755 -0.34906585  0.34906585
# # 1.04719755  1.74532925  2.44346095  3.14159265]
print (x[::-1])
# # [ 3.14159265  2.44346095  1.74532925  1.04719755  0.34906585 -0.34906585
# #  -1.04719755 -1.74532925 -2.44346095 -3.14159265]



# # Matrices
# # A matrix is a 2-dimensional array of numbers written between square brackets.

# # Defining a matrix in Python
import numpy as np
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(X)
# # [[1 2 3]
# #  [4 5 6]
# #  [7 8 9]]
Y = np.mat([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(Y)
# # [[1 2 3]
# #  [4 5 6]
# #  [7 8 9]]

# # Matrix indexing
print (X[0, 0])
# # 1
print (X[-1, -1])
# # 9
print (X[0, :])
# # [1 2 3]
print (X[:, 0])
# # [1 4 7]
print (X[:])
# # [[1 2 3]
# #  [4 5 6]
# #  [7 8 9]]

# # use indexing to address and assign new values to elements of a matrix
X[:, 0] = [11, 12, 13]  
X[2, 2] = 15  
print (X)
# # [[11  2  3]
# #  [12  5  6]
# #  [13  8 15]]

X[2] = 16
print (X)
# # [[11  2  3]
# #  [12  5  6]
# #  [16 16 16]]

X[:,2] = 17
print (X)
# # [[11  2 17]
# #  [12  5 17]
# #  [16 16 17]]


# # Shape of an array
# # The shape (or "dimensions") of a vector/matrix array tells us
# # the number of values for each dimension.
print(X.shape)
# # (3, 3)


# # Transposition
# # Using transposition, you can convert a row vector to a column vector and vice versa. 
import numpy as np

A = np.array([
   [1, 2, 3], 
   [4, 5, 6],
   [7, 8, 9]])

A_transposed = A.T
A_transposed_2 = np.transpose(A)

print(A,'\n\n', A_transposed, '\n\n', A_transposed_2)

# # [[1 2 3]
# #  [4 5 6]
# #  [7 8 9]] 

# #  [[1 4 7]
# #  [2 5 8]
# #  [3 6 9]]

# #  [[1 4 7]
# #  [2 5 8]
# #  [3 6 9]]



# Tensors
# An array of numbers arranged on a regular grid with a 
# variable number of axes is known as a tensor.
# Tensor is like a function, i.e. is linear in nature. It describes an object that is in space. Tensors are of different types –

# 0 Rank tensors – Scalars
# 1st Rank tensors – 1-D arrays 
# 2nd Rank tensors – 2-D arrays (A matrix)
# nth Rank tensors – n-D arrays 

# # 1D Tensor (Vector) 
import numpy as np
x = np.array([56, 183, 1])
# #
# # Dimension = 1
# # Shape = 1,
# #
print(x.ndim, x.shape)
# # 1 (3,)


# # 2D Tensor (Matrix)
import numpy as np
x = np.array([[56, 183, 1],
             [78, 178, 2],
             [50, 165, 0]])
# #
# # Dimension = 2
# # Shape = 3, 3
# #
print(x.ndim, x.shape)
# # 2 (3, 3)


# 3D Tensor
import numpy as np
x = np.array([[[56, 183, 1],
               [65, 164, 0]],
              [[85, 176, 1],
               [44, 164, 0]]])
#
# Dimension = 3
# Shape = (2, 3, 3),
#
print(x.ndim, x.shape)
# 3 (2, 2, 3)
