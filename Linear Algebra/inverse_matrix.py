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



# # Solution 3 - NumPy
import numpy as np
  
A = np.array([[[1., 2.], [3., 4.]],
              [[1, 3], [3, 5]]])
  
print(np.linalg.inv(A))

# # Output:
# # [[[-2.    1.  ]
# #   [ 1.5  -0.5 ]]

# #  [[-1.25  0.75]
# #   [ 0.75 -0.25]]]


# # Solution 4 - NumPy
# # linalg.inv(a): Compute the (multiplicative) inverse of a matrix.
import numpy as np
from numpy.linalg import inv

a = np.array([[1., 2.], [3., 4.]])

ainv = inv(np.matrix(a))

print(ainv)

# # Output:
# # [[-2.   1. ]
# #  [ 1.5 -0.5]]



# # Solution 5 - NumPy (3*3)
# # linalg.inv(a): Compute the (multiplicative) inverse of a matrix.
import numpy as np
from numpy.linalg import inv

a = np.array([[3, 0, 2],
              [2, 0, -2],
              [0, 1, 1]])

ainv = inv(np.matrix(a))

print(ainv)

# # Output:
# # [[ 0.2  0.2  0. ]
# #  [-0.2  0.3  1. ]
# #  [ 0.2 -0.3 -0. ]]



# mathematical logic for calculating an inverse matrix
def return_transpose(mat):
    return map(list,zip(*mat))

def return_matrix_minor(mat,i,j):
    return [row[:j] + row[j+1:] for row in (mat[:i]+mat[i+1:])]

def return_determinant(mat):
    if len(mat) == 2:
        return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*return_determinant(return_matrix_minor(m,0,c))
    return determinant

def inverse_matrix(m):
    determinant = return_determinant(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    cfs = []
    for r in range(len(m)):
        cfRow = []
        for c in range(len(m)):
            minor = return_matrix_minor(m,r,c)
            cfRow.append(((-1)**(r+c)) * return_determinant(minor))
        cfs.append(cfRow)
    cfs = return_transpose(cfs)
    for r in range(len(cfs)):
        for c in range(len(cfs)):
            cfs[r][c] = cfs[r][c]/determinant
    return cfs

m = [[4,3],[8,5]]
print(inverse_matrix(m))

# Output:
# [[-1.25, 0.75], [2.0, -1.0]]
