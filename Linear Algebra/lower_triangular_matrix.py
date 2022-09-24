# Code by AmirMotefaker

# Lower Triangular Matrix:
# A square matrix is called lower triangular if all the entries above the main diagonal are zero. 

# # Solution 1
def islowertriangular(M):
    for i in range(0, len(M)):
        for j in range(i + 1, len(M)):
            if(M[i][j] != 0):
                    return False
    return True
     
M = [[1,0,0,0],
     [1,4,0,0],
     [4,6,2,0],
     [0,4,7,6]]
 
if islowertriangular(M):
    print ("Yes")
else:
    print ("No")

# # Output:
# # Yes



# # Solution 2 - numpy.tril
# # numpy.tril(m, k=0): Lower triangle of an array.

import numpy as np

print(np.tril([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], -1))

# # Output:
# # [[ 0  0  0]
# #  [ 4  0  0]
# #  [ 7  8  0]
# #  [10 11 12]]



# Solution 3 - numpy.tril
import numpy as np

print(np.tril(np.arange(3*4*5).reshape(3, 4, 5)))

# Output:
# [[[ 0  0  0  0  0]
#   [ 5  6  0  0  0]
#   [10 11 12  0  0]
#   [15 16 17 18  0]]

#  [[20  0  0  0  0]
#   [25 26  0  0  0]
#   [30 31 32  0  0]
#   [35 36 37 38  0]]

#  [[40  0  0  0  0]
#   [45 46  0  0  0]
#   [50 51 52  0  0]
#   [55 56 57 58  0]]]
