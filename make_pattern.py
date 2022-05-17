# Code by amotef@gmail.com

# Make Pattern

## Simple pyramid pattern

n = int(input("Enter the number of rows :"))  
for i in range(0, n):  
    for j in range(0, i + 1):  
        print("* ", end="")       
    print()  


## Output ( for row = 5)
# * 
# * * 
# * * * 
# * * * * 
# * * * * *

