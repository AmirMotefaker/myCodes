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

def pyr_pat_deg(n):
     
    k = 2*n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
     
        k = k - 2           # decrementing k after each loop
     
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

