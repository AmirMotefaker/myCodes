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

