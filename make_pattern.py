# Code by @AmirMotefaker

# Make Pattern

### Simple pyramid pattern

n = int(input("Enter the number of rows : "))  
for i in range(0, n):  
    for j in range(0, i + 1):  
        print("* ", end="")       
    print()  


## Output (row = 5)
# * 
# * * 
# * * * 
# * * * * 
# * * * * *



### Simple pyramid pattern with using list

def pyramid_pattern(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))
 
n = int(input("Enter the number of rows : ")) 
pyramid_pattern(n)


## Output (row = 5)
# *
# **
# ***
# ****
# *****



### Simple pyramid pattern with 180 degree rotation

def pyr_pat_deg(n):
     
    k = 2*n - 2    # number of spaces
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
     
        k = k - 2  # decrementing k after each loop
     
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
 
n = int(input("Enter the number of rows : "))
pyr_pat_deg(n)


## Output (row = 5)
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *



### Simple pyramid pattern Triangle

def triangle(n):
     
    k = n - 1   # number of spaces
 
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
     
        k = k - 1
     
        for j in range(0, i+1):
            print("* ", end="")
     
        print("\r")
 
n = int(input("Enter the number of rows : "))
triangle(n)


## Output (row = 5)
#     *
#    * *
#   * * *
#  * * * *
# * * * * *


### Reverse Pyramid Pattern

def pattern_rev(n):
      k = 2*n -2
      for i in range(n,-1,-1):
           for j in range(k,0,-1):
                print(end=" ")
           k = k +1
           for j in range(0, i+1):
                print("*", end=" ")
           print()

n = int(input("Enter the number of rows : ")) 
pattern_rev(n)


## Output (row = 5)
# * * * * * * 
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *


### Right Start Pattern

def pattern_right(n):
      for i in range(0, n):
            for j in range(0, i + 1):
                print("* ", end="")
            print()
      for i in range(n, 0 , -1):
            for j in range(0, i + 1):
               print("* ", end="")
            print()
 
n = int(input("Enter the number of rows : "))
pattern_right(n)


## Output (row = 5)
# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *



### Left Start Pattern

def pattern_left(n):
    k = 2 * n - 2
    for i in range(0, n-1):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print()
    k = -1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print()
 
n = int(input("Enter the number of rows : ")) 
pattern_left(n)


## Output (row = 5)
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *



### Hourglass Pattern 

def pattern_hourglass(n):
    
    k = n - 2
    for i in range(n, -1 , -1):
        for j in range(k , 0 , -1):
            print(end=" ")
        k = k + 1    
        for j in range(0, i+1):
            print("* " , end="")
        print()
    
    k = 2 * n  - 2
    for i in range(0 , n+1):
        for j in range(0 , k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print()
 
n = int(input("Enter the number of rows : "))
pattern_hourglass(n)


## Output (row = 5)
#    * * * * * * 
#     * * * * *
#      * * * *
#       * * *
#        * *
#         *
#         *
#        * *
#       * * *
#      * * * *
#     * * * * *
#    * * * * * *



### Diamond Shaped Pattern

def pattern_diamond(n):
     k = 2 * n - 2
     for i in range(0, n):
          for j in range(0 , k):
               print(end=" ")
          k = k - 1
          for j in range(0 , i + 1 ):
               print("* ", end="")
          print()
     k = n - 2
     for i in range(n , -1, -1):
        for j in range(k , 0 , -1): 
            print(end=" ")
        k = k + 1
        for j in range(0 , i + 1):
            print("* ", end="")
        print()
 
n = int(input("Enter the number of rows : "))
pattern_diamond(n)


## Output (row = 5)
#         * 
#        * *
#       * * *
#      * * * *
#     * * * * *
#    * * * * * *
#     * * * * *
#      * * * *
#       * * * 
#        * *
#         *



### Hollow Diamond pattern

row = int(input('Enter number of row: '))

# The upper part of the Diamond
for i in range(1, row+1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# The bottom of the Diamond
for i in range(row-1,0, -1):
    for j in range(1,row-i+1):
        print(" ", end="")
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


## Output (row = 5)
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *



### Number Pattern

def num_pat(n):
     
    num = 1   # starting number
 
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1   # incrementing number at each column
        print("\r")
 
n = int(input("Enter the number of rows : "))
num_pat(n)


## Output (row = 5)
# 1 
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5



### Number Pattern without reassigning(count number)

def count_num(n):
     
    num = 1
 
    for i in range(0, n):
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
 
n = int(input("Enter the number of rows : "))
count_num(n)


## Output (row = 5)
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15



### Character Pattern

def alphabet(n):
     
    num = 65   # initializing value corresponding to 'A'
 
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)   # converting to char
            print(ch, end=" ")
        num = num + 1
        print("\r")
 
n = int(input("Enter the number of rows : "))
alphabet(n)


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
