# Code by @AmirMotefaker

# OOP - Polymorphism

# # Solution 1 - Area Square
# class Shape:  #  Abstract Class
#     def __init__(self, kind, name):
#         self.kind = kind
#         self.name = name

#     def area(self):
#         raise NotImplementedError('All children of Shape class should redefine the area method.')

# class Square(Shape):
#     def __init__(self, kind, name, side_length):
#         super().__init__(kind, name)
#         self.side_length = side_length

#     def area(self):
#         return self.side_length ** 2


# square = Square('square', 'a', 4 )
# print(square.area())

# # Output:
# # 16



# # Solution 2 - Area(Square, Circle)
# class Shape:  #  Abstract Class
#     def __init__(self, kind, name):
#         self.kind = kind
#         self.name = name

#     def area(self):
#         raise NotImplementedError('All children of Shape class should redefine the area method.')

# class Circle(Shape):
#     pi = 3.14

#     def __init__(self, kind, name, r):
#         super().__init__(kind, name)
#         self.radius = r

#     def area(self):  # Override
#         return Circle.pi * (self.radius ** 2) 

# class Square(Shape):
#     def __init__(self, kind, name, side_length):
#         super().__init__(kind, name)
#         self.side_length = side_length

#     def area(self):
#         return self.side_length ** 2


# square = Square('square', 'a', 10 )
# circle = Circle('circle', 'b', 10)
# print(square.area())  # Polymorphism
# print(circle.area())

# # Output:
# # 100
# # 314.0



# # Solution 3 - Area(Square, Circle)
# class Shape:  #  Abstract Class
#     def __init__(self, kind, name):
#         self.kind = kind
#         self.name = name

#     def area(self):
#         raise NotImplementedError('All children of Shape class should redefine the area method.')

# class Circle(Shape):
#     pi = 3.14

#     def __init__(self, kind, name, r):
#         super().__init__(kind, name)
#         self.radius = r

#     def area(self):  # Override
#         return Circle.pi * (self.radius ** 2) 

# class Square(Shape):
#     def __init__(self, kind, name, side_length):
#         super().__init__(kind, name)
#         self.side_length = side_length

#     def area(self):
#         return self.side_length ** 2


# def show_area(s):
#     print(s.area())

# square = Square('square', 'a', 10 )
# circle = Circle('circle', 'b', 10)

# show_area(square)
# show_area(circle)

# # Output:
# # 100
# # 314.0



# # Solution 4 - Area(Square1, Circle1, Circle2)
# class Shape:  #  Abstract Class
#     def __init__(self, kind, name):
#         self.kind = kind
#         self.name = name

#     def area(self):
#         raise NotImplementedError('All children of Shape class should redefine the area method.')

# class Circle(Shape):
#     pi = 3.14

#     def __init__(self, kind, name, r):
#         super().__init__(kind, name)
#         self.radius = r

#     def area(self):  # Override
#         return Circle.pi * (self.radius ** 2) 

# class Square(Shape):
#     def __init__(self, kind, name, side_length):
#         super().__init__(kind, name)
#         self.side_length = side_length

#     def area(self):
#         return self.side_length ** 2


# def show_area(s):
#     print(s.area())


# square1 = Square('square', 'a', 10 )
# circle1 = Circle('circle', 'b', 10)
# circle2 = Circle('circle', 'c', 4)

# for shape in [square1, circle1, circle2]:
#     show_area(shape)


# # Output:
# # 100
# # 314.0
# # 50.24



# Solution 5 - Area(Square1, Circle1, Circle2)
class Shape:  #  Abstract Class
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def area(self):
        raise NotImplementedError('All children of Shape class should redefine the area method.')

class Circle(Shape):
    pi = 3.14

    def __init__(self, name, r):
        super().__init__('circle', name)
        self.radius = r

    def area(self):  # Override
        return Circle.pi * (self.radius ** 2) 

class Square(Shape):
    def __init__(self, name, side_length):
        super().__init__('square', name)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


def show_area(s):
    print(s.area())


square1 = Square('a', 10 )
circle1 = Circle('b', 10)
circle2 = Circle('c', 4)

for shape in [square1, circle1, circle2]:
    show_area(shape)

# Output:
# 100
# 314.0
# 50.24
