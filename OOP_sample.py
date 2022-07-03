# Code by @AmirMotefaker

# object-oriented Programming (OOPs)

# # Solution 1
# class Car:
#     def __init__(self, car_color):
#         self.color = car_color  # instance attribute

# car1= Car('blue')  # instance
# car2= Car('yellow')
# car3= Car('red')   # instance

# print(car1.color)
# print(car2.color)

# # Output:
# # blue
# # yellow


# Solution 2
class Car:
    def __init__(self, color, model):  # constructor
        self.color = color  # instance attribute
        self.model = model

car1= Car('blue', 'BMW')  # instance
car2= Car('yellow', 'AUDI')
car3= Car('red', 'BMW')   # instance

print(car1.color)
print(car1.model)
print(car2.color)
print(car2.model)

# Output:
# blue
# BMW
# yellow
# AUDI
