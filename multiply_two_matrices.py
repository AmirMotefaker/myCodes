# Code by @AmirMotefaker

# Multiply Two Matrices


# Solution 1

# X = 3x3 matrix
# Y = 3x4 matrix
# result is 3x4


# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]
# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]

# for i in range(len(X)):
#    for j in range(len(Y[0])):
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]

# for r in result:
#    print(r)


# Solution 2
# Matrix Multiplication Using Nested List Comprehension

# Program to multiply two matrices using list comprehension

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)

