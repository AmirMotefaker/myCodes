# Code by @AmirMotefaker

# object-oriented Programming (OOPs)

class Car:
    def __init__(self, car_color):
        self.color = car_color  # instance attribute

car1= Car('blue')  # instance
car2= Car('yellow')
car3= Car('red')   # instance

print(car1.color)
print(car2.color)

# Output:
# blue
# yellow
