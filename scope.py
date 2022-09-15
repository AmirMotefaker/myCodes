# Code by @AmirMotefaker

# Scope in Python

## Solution 1
a = 1

def my_function1():
    a = 2
    print(a)

def my_function2():
    a = 3
    print(a)

print(a)
my_function1()
print(a)
my_function2()
print(a)

# Output:
# 1
# 2
# 1
# 3
# 1


## Solution  2
a = 1
b = 2
c = 3

def print_abc():
    a = 55
    print(a)
    b = 66
    print(b)

print(a)
print(b)
print_abc()
print(a)
print(b)

# Output:
# 1
# 2 
# 55
# 66
# 1 
# 2 
