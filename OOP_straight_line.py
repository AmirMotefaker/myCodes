# Code by @AmirMotefaker

# OOP - Construction of straight line class

# # Solution 1
# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2

#     def __str__(self):
#         return f'Line: a=({self.x1},{self.y1}) b=({self.x2},{self.y2})'


# line1 = Line(1,1,3,3)

# print(line1)

# # Output:
# # Line: a=(1,1) b=(3,3)



# # Solution 2
# class Line:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
     
#     def __str__(self):
#         return f'Line: a=({self.a[0]},{self.a[1]}) b=({self.b[0]},{self.b[1]})'


# line1 = Line((1,1), (3,3))

# print(line1)

# # Output:
# # Line: a=(1,1) b=(3,3)



# # Solution 3 - with length
# class Line:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
     
#     def __str__(self):
#         return f'Line: a=({self.a[0]},{self.a[1]}) b=({self.b[0]},{self.b[1]})'

#     def length(self):
#         return ((self.b[1] - self.a[1]) ** 2 + (self.b[0] - self.a[0]) ** 2) ** 0.5


# line1 = Line((0,0), (3,3))

# print(line1.length())

# # for Test
# print(18 ** 0.5)

# # Output:
# # 4.242640687119285
# # 4.242640687119285



# Solution 4 - Slope(shib)
class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b
     
    def __str__(self):
        return f'Line: a=({self.a[0]},{self.a[1]}) b=({self.b[0]},{self.b[1]})'

    def length(self):
        return ((self.b[1] - self.a[1]) ** 2 + (self.b[0] - self.a[0]) ** 2) ** 0.5

    def slope(self):
        return (self.b[1] - self.a[1]) / (self.b[0] - self.a[0])

line1 = Line((0,0), (3,3))

print(line1.length())
print(line1.slope())

# Output:
# 4.242640687119285
# 1.0
