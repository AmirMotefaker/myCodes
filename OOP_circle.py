# Code by @AmirMotefaker

# OOP - Circle

# # Solution 1
# class Circle:
#     pi = 3.14  # Class Attribute

#     def __init__(self, r):
#         self.r = r

#     def calc_diameter(self):
#         return self.r * 2

# circle1 = Circle(10)
# circle2 = Circle(20)

# print(circle1.pi)
# print(circle1.r)
# print(circle2.r)

# print(circle1.calc_diameter())

# # Output:
# # 3.14
# # 10
# # 20
# # 20



# # Solution 2 - Area
# class Circle:
#     pi = 3.14  # Class Attribute

#     def __init__(self, r):
#         self.r = r

#     def calc_diameter(self):
#         return self.r * 2

#     def calc_area(self):
#         # pi * (r ** 2)
#         return self.pi * (self.r ** 2)

  
# circle1 = Circle(14)

# print(circle1.calc_diameter())
# print(circle1.calc_area())

# # Output:
# # 28
# # 615.44



# # Solution 3 - circumference
# class Circle:
#     pi = 3.14  # Class Attribute

#     def __init__(self, r):
#         self.r = r

#     def calc_diameter(self):
#         return self.r * 2

#     def calc_area(self):
#         # pi * (r ** 2)
#         return self.pi * (self.r ** 2)

#     def calc_circumference(self):
#         # 2 * pi * r
#         return 2 * self.pi * self.r 

# circle1 = Circle(14)

# print(circle1.calc_diameter())
# print(circle1.calc_area())
# print(circle1.calc_circumference())

# # Output:
# # 28
# # 615.44
# # 87.92


# # Solution 4 - Area and circumference
# class Circle:
#     pi = 3.14  # Class Attribute

#     def __init__(self, r):
#         self.r = r

#     def calc_diameter(self):
#         return self.r * 2

#     def calc_area(self):
#         return self.pi * (self.r ** 2)

#     def calc_circumference(self):
#         return 2 * Circle.pi * self.r 

# circle1 = Circle(10)
# print(circle1.calc_area())
# circle1.pi = 3.1415
# print(circle1.calc_area())

# # Output:
# # 314.0
# # 314.15000000000003


# Solution 5 - Area and circumference
class Circle:
    pi = 3.14  # Class Attribute

    def __init__(self, r):
        self.r = r

    def calc_diameter(self):
        return self.r * 2

    def calc_area(self):
        return Circle.pi * (self.r ** 2)

    def calc_circumference(self):
        return 2 * Circle.pi * self.r 

circle1 = Circle(10)
print(circle1.calc_area())
circle1.pi = 3.14159265359
print(circle1.calc_area())

# Output:
# 314.0
# 314.0
