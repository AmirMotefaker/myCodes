# Code by amotef@gmail.com

# Make Pattern

### Simple pyramid pattern

# n = int(input("Enter the number of rows : "))  
# for i in range(0, n):  
#     for j in range(0, i + 1):  
#         print("* ", end="")       
#     print()  


## Output (row = 5)
# * 
# * * 
# * * * 
# * * * * 
# * * * * *



### Simple pyramid pattern with using list

# def pyramid_pattern(n):
#     myList = []
#     for i in range(1,n+1):
#         myList.append("*"*i)
#     print("\n".join(myList))
 
# n = int(input("Enter the number of rows : ")) 
# pyramid_pattern(n)


## Output (row = 5)
# *
# **
# ***
# ****
# *****



### Simple pyramid pattern with 180 degree rotation

# def pyr_pat_deg(n):
     
#     k = 2*n - 2       # number of spaces
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
     
#         k = k - 2           # decrementing k after each loop
     
#         for j in range(0, i+1):
#             print("* ", end="")
#         print("\r")
 
# n = int(input("Enter the number of rows : "))
# pyr_pat_deg(n)


## Output (row = 5)
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *



### Simple pyramid pattern Triangle

# def triangle(n):
     
#     k = n - 1       # number of spaces
 
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
     
#         k = k - 1
     
#         for j in range(0, i+1):
#             print("* ", end="")
     
#         print("\r")
 
# n = int(input("Enter the number of rows : "))
# triangle(n)


## Output (row = 5)
#     *
#    * *
#   * * *
#  * * * *
# * * * * *



### Number Pattern

# def num_pat(n):
     
#     num = 1   # starting number
 
#     for i in range(0, n):
#         num = 1
#         for j in range(0, i+1):
#             print(num, end=" ")
#             num = num + 1   # incrementing number at each column
#         print("\r")
 
# n = int(input("Enter the number of rows : "))
# num_pat(n)


## Output (row = 5)
# 1 
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5



### Number Pattern without reassigning(count number)

# def count_num(n):
     
#     num = 1
 
#     for i in range(0, n):
#         for j in range(0, i+1):
#             print(num, end=" ")
#             num = num + 1
#         print("\r")
 
# n = int(input("Enter the number of rows : "))
# count_num(n)


## Output (row = 5)
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15



### Character Pattern

# def alphabet(n):
     
#     num = 65   # initializing value corresponding to 'A'
 
#     for i in range(0, n):
#         for j in range(0, i+1):
#             ch = chr(num)   # converting to char
#             print(ch, end=" ")
#         num = num + 1
#         print("\r")
 
# n = int(input("Enter the number of rows : "))
# alphabet(n)


## Output (row = 5)
# A 
# B B 
# C C C
# D D D D
# E E E E E



### Continuous Character pattern

def  count_alpha(n):
     
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ")
            num = num +1
        print("\r")

n = int(input("Enter the number of rows : "))
count_alpha(n)


## Output (row = 5)
# A 
# B C
# D E F
# G H I J
# K L M N O
