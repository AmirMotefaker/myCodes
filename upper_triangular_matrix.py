# Code by @AmirMotefaker

# Upper Triangular Matrix:
# A square matrix is called upper triangular if all the entries below the main diagonal are zero.

# # Solution 1
def isuppertriangular(M):
    for i in range(1, len(M)):
        for j in range(0, i):
            if(M[i][j] != 0):
                    return False
    return True
     
# Driver function.
M = [[1,3,5,3],
    [0,4,6,2],
    [0,0,2,5],
    [0,0,0,6]]
 
if isuppertriangular(M):
    print ("Yes")
else:
    print ("No")

# # Output:
# # Yes



# Solution 2 - numpy.triu
# numpy.triu(m, k=0): Upper triangle of an array.
import numpy as np

print(np.triu([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], -1))

# Output:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 0  8  9]
#  [ 0  0 12]]

  

# Solution 3 - numpy.triu
import numpy as np

print(np.triu(np.arange(3*4*5).reshape(3, 4, 5)))

# Output:
# [[[ 0  1  2  3  4]
#   [ 0  6  7  8  9]
#   [ 0  0 12 13 14]
#   [ 0  0  0 18 19]]

#  [[20 21 22 23 24]
#   [ 0 26 27 28 29]
#   [ 0  0 32 33 34]
#   [ 0  0  0 38 39]]

#  [[40 41 42 43 44]
#   [ 0 46 47 48 49]
#   [ 0  0 52 53 54]
#   [ 0  0  0 58 59]]]

