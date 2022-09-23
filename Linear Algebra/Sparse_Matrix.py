# Code by AmirMotefaker

# Sparse Matrix 

# If most of the elements of the matrix have 0 value, then it is called a sparse matrix.

# # Solution 1 - NumPy, SciPy
# # sparse matrix using csr_matrix()
import numpy as np
from scipy.sparse import csr_matrix
  
sparseMatrix = csr_matrix((3, 4), 
                          dtype = np.int8).toarray()
  
print(sparseMatrix)

# # Output:
# # [[0 0 0 0]
# #  [0 0 0 0]
#  [0 0 0 0]]



# # Solution 2 - NumPy, SciPy
import numpy as np
from scipy.sparse import csr_matrix
  
row = np.array([0, 0, 1, 1, 2, 1])
col = np.array([0, 1, 2, 0, 2, 2])
  
data = np.array([1, 4, 5, 8, 9, 6])
  
sparseMatrix = csr_matrix((data, (row, col)), 
                          shape = (3, 3)).toarray()
  
print(sparseMatrix)

# # Output:
# # [[ 1  4  0]
# #  [ 8  0 11]
# #  [ 0  0  9]]



# # Solution 3 - NumPy, SciPy
import numpy as np
from scipy.sparse import csc_matrix
  
sparseMatrix = csc_matrix((3, 4), 
                          dtype = np.int8).toarray()
  
print(sparseMatrix)

# # Output:
# # [[0 0 0 0]
# #  [0 0 0 0]
# #  [0 0 0 0]]



# Solution 4 - NumPy, SciPy
import numpy as np
from scipy.sparse import csc_matrix
  
row = np.array([0, 0, 1, 1, 2, 1])
col = np.array([0, 1, 2, 0, 2, 2])
  
data = np.array([1, 4, 5, 8, 9, 6])
  
sparseMatrix = csc_matrix((data, (row, col)),
                          shape = (3, 3)).toarray()
  
print(sparseMatrix)

# Output:
# [[ 1  4  0]
#  [ 8  0 11]
#  [ 0  0  9]]
