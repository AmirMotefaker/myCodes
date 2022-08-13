# Code by @AmirMotefaker

# Transpose a Matrix


# # Solution 1 - Square Matrix
N = 4
 
def transpose(A,B):
    for i in range(N):
        for j in range(N):
            B[i][j] = A[j][i]
 
A = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]
 
 
B = A[:][:] 
 
transpose(A, B)
 
print("Result matrix is")
for i in range(N):
    for j in range(N):
        print(B[i][j], " ", end='')
    print()

# # Output:
# # Result matrix is
# # 1  2  3  4
# # 2  2  3  4
# # 3  3  3  4
# # 4  4  4  4



# # Solution 2 - Rectangular Matrix
M = 3
N = 4
 
def transpose(A, B):
 
    for i in range(N):
        for j in range(M):
            B[i][j] = A[j][i]
 
A = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3]]
 
B = [[0 for x in range(M)] for y in range(N)]
 
transpose(A, B)
 
print("Result matrix is")
for i in range(N):
    for j in range(M):
        print(B[i][j], " ", end='')
    print() 

# # Output:
# # Result matrix is
# # 1  2  3
# # 1  2  3
# # 1  2  3
# # 1  2  3



# # Solution 3 - In-Place for Square Matrix:
N = 4
 
def transpose(A):
 
    for i in range(N):
        for j in range(i+1, N):
            A[i][j], A[j][i] = A[j][i], A[i][j]
 
A = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]
 
transpose(A)
 
print("Modified matrix is")
for i in range(N):
    for j in range(N):
        print(A[i][j], " ", end='')
    print()

# # Output:
# # Modified matrix is
# # 1  2  3  4
# # 1  2  3  4
# # 1  2  3  4
# # 1  2  3  4



# # Solution 4 - Transpose of matrix
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)

# # Output:
# # [12, 4, 3]
# # [7, 5, 8]




# # Solution 5 - Transpose of matrix with NumPy 
import numpy as np
              
gfg = np.matrix('[4, 1; 12, 3]')
              
trans = gfg.transpose()
    
print(trans)

# # Output:
# # [[ 4 12]
# #  [ 1  3]]




# Solution 6 - Transpose of matrix with NumPy 
import numpy as np
              
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')
              
trans = gfg.transpose()
    
print(trans)

# Output:
# [[ 4 12  4]
#  [ 1  3  5]
#  [ 9  1  6]]
