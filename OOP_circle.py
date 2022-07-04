# Code by @AmirMotefaker

# OOP - Circle

class Circle:
    pi = 3.14  # Class Attribute

    def __init__(self, r):
        self.r = r

    def calc_diameter(self):
        return self.r * 2

circle1 = Circle(10)
circle2 = Circle(20)

print(circle1.pi)
print(circle1.r)
print(circle2.r)

print(circle1.calc_diameter())

# Output:
# 3.14
# 10
# 20
# 20


