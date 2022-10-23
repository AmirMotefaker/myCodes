# Code by AmirMotefaker

# Swap Two Variables

# Solution 1 - Using Temporary Variable
x = 5
y = 10

# To take inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# Output:
# Enter value of x: 5
# Enter value of y: 10
# The value of x after swapping: 10
# The value of y after swapping: 5



## Solution 2 - Without Using Temporary Variable

x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)

# Output
# x = 10
# y = 5
