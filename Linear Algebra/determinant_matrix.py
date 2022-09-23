# Code by @AmirMotefaker

# Determinant Calculation

# # Solution 1 - Determinant of 2 x 2 Matrix
 
# # defining a function to get the minor matrix after 
# # excluding i-th row and j-th column.
def getcofactor(m, i, j):
    return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]
 
# defining the function to calculate determinant value
# of given matrix a.
def determinantOfMatrix(mat):
    if(len(mat) == 2):
        value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return value
 
    Sum = 0
 
    # traverse each column of matrix a.
    for current_column in range(len(mat)):
 
        # calculating the sign corresponding to co-factor of that sub matrix.
        sign = (-1) ** (current_column)
 
        # calling the function recursily to get determinant value of
        # sub matrix obtained.
        sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))
 
        # adding the calculated determinant value of particular column
        # matrix to total Sum.
        Sum += (sign * mat[0][current_column] * sub_det)
 
    return Sum
 
if __name__ == '__main__':
 
    mat = [[1, 0, 2, -1],
           [3, 0, 0, 5],
           [2, 1, 4, -3],
           [1, 0, 5, 0]]
 
    print('Determinant of the matrix is :', determinantOfMatrix(mat))
 
# # Output:
# # Determinant of the matrix is : 30




# # Solution 2 - Adjoint and Inverse of a Matrix 
def determinantOfMatrix(mat, n):
 
    temp = [0]*n  # temporary array for storing row
    total = 1
    det = 1  # initialize result
 
    # loop for traversing the diagonal elements
    for i in range(0, n):
        index = i 
 
        # finding the index which has non zero value
        while(index < n and mat[index][i] == 0):
            index += 1
 
        if(index == n):  # if there is non zero element
            # the determinant of matrix as zero
            continue
 
        if(index != i):
            # loop for swapping the diagonal element row and index row
            for j in range(0, n):
                mat[index][j], mat[i][j] = mat[i][j], mat[index][j]
 
            # determinant sign changes when we shift rows
            # go through determinant properties
            det = det*int(pow(-1, index-i))
 
        # storing the values of diagonal row elements
        for j in range(0, n):
            temp[j] = mat[i][j]
 
        # traversing every row below the diagonal element
        for j in range(i+1, n):
            num1 = temp[i]     # value of diagonal element
            num2 = mat[j][i]   # value of next row element
 
            # traversing every column of row
            # and multiplying to every row
            for k in range(0, n):
                # multiplying to make the diagonal
                # element and next row element equal
 
                mat[j][k] = (num1*mat[j][k]) - (num2*temp[k])
 
            total = total * num1  # Det(kA)=kDet(A);
 
    # multiplying the diagonal elements to get determinant
    for i in range(0, n):
        det = det*mat[i][i]
 
    return int(det/total)  # Det(kA)/k=Det(A);
 
 
if __name__ == "__main__":
 
    mat = [[1, 0, 2, -1], [3, 0, 0, 5], [2, 1, 4, -3], [1, 0, 5, 0]]
    N = len(mat)
     
    print("Determinant of the matrix is : ", determinantOfMatrix(mat, N))

# # Output:
# # Determinant of the matrix is :  30




# Solution 3 - NumPy
import numpy as np
 
def determinant(mat):
     
    det = np.linalg.det(mat)
    return round(det)
 
mat = [[1, 0, 2, -1],
       [3, 0, 0, 5],
       [2, 1, 4, -3],
       [1, 0, 5, 0]]
 
print('Determinant of the matrix is:',
      determinant(mat))
 
# Output:
# Determinant of the matrix is: 30
