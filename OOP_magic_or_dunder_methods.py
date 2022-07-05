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



# # Solution 2
# class Square:

#     def __init__(self, side_length):
#         self.s = side_length

#     def __str__(self):
#         return f'Square with side length of {self.s}'

    
# square = Square(10)

# print(square)

# # Output:
# # Square with side length of 10



# # Solution 3
# class Square:

#     def __init__(self, side_length):
#         self.s = side_length

#     def __str__(self):
#         return f'Square with side length of {self.s}'

    
# square = Square(10)
# s1 = Square(99)

# print(square)
# print(s1)

# # Output:
# # Square with side length of 10
# # Square with side length of 99 



# # Solution 4
# class Square:

#     def __init__(self, side_length):
#         self.s = side_length

#     def __str__(self):
#         return f'Square with side length of {self.s}'

#     def __len__(self):
#         return 4 * self.s
    
# square = Square(10)
# #s1 = Square(99)
# print(len(square))

# # Output:
# # 40



# Solution 5
class Square:

    def __init__(self, side_length):
        self.s = side_length

    def __str__(self):
        return f'Square with side length of {self.s}'

    def __len__(self):
        return 4 * self.s

    def __del__(self):
        print( f'Square with {self.s} side length is deleted.')

    
square = Square(10)
del square

# Output:
# Square with 10 side length is deleted.
