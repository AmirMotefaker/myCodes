# Code by @AmirMotefaker

# OOP - Polymorphism

# Solution 1
class Shape:  #  Abstract Class
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name

    def area(self):
        raise NotImplementedError('All children of Shape class should redefine the area method.')

class Square(Shape):
    def __init__(self, kind, name, side_length):
        super().__init__(kind, name)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


square = Square('square', 'a', 4 )
print(square.area())

# Output:
# 16
