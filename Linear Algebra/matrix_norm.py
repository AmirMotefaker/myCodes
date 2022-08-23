# Code by @AmirMotefaker

# Matrix norm

# # Solution 1
# # computes the vector norm of a vector of dimension (1, 10)
import numpy as np
 
vec = np.arange(10)
 
vec_norm = np.linalg.norm(vec)
 
print("Vector norm:")
print(vec_norm)

# # Output:
# # Vector norm:
# # 16.881943016134134



# # Solution 2
# # matrix norm for a matrix of dimension (2, 3)
import numpy as np
 
mat = np.array([[ 1, 2, 3],
               [4, 5, 6]])
 
mat_norm = np.linalg.norm(mat)
 
print("Matrix norm:")
print(mat_norm)

# # Output:
# # Matrix norm:
# # 9.539392014169456


# # Solution 3
# # To compute matrix norm along a particular axis 
import numpy as np
 
mat = np.array([[ 1, 2, 3],
               [4, 5, 6]])
 
mat_norm = np.linalg.norm(mat, axis = 1)
 
print("Matrix norm along particular axis :")
print(mat_norm)

# # Output:
# # Matrix norm along particular axis :
# # [3.74165739 8.77496439]



# Solution 4
# convert a vector into a matrix, or if both have same elements
# then their norm will be equal too.
import numpy as np
 
vec = np.arange(9)
 
mat = vec.reshape((3, 3))
 
vec_norm = np.linalg.norm(vec)
 
print("Vector norm:")
print(vec_norm)
 
mat_norm = np.linalg.norm(mat)
 
print("Matrix norm:")
print(mat_norm)
 
# Output:
# Vector norm:
# 14.2828568570857
# Matrix norm:
# 14.2828568570857
