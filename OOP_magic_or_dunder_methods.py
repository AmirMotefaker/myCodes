# Code by @AmirMotefaker

# OOP - Magic or Dunder Methods

# # Solution 1
# class Square:

#     def __init__(self, side_length):
#         self.s = side_length

    
# square = Square(10)

# print(square.s)

# # Output:
# # 10



# Solution 2
class Square:

    def __init__(self, side_length):
        self.s = side_length

    def __str__(self):
        return f'Square with side length of {self.s}'

    
square = Square(10)

print(square)

# Output:
# Square with side length of 10
