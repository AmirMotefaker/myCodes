# Code by @AmirMotefaker

# OOP - Construction of straight line class

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f'Line: a=({self.x1},{self.y1}) b=({self.x2},{self.y2})'


line1 = Line(1,1,3,3)

print(line1)

# Output:
# Line: a=(1,1) b=(3,3)
