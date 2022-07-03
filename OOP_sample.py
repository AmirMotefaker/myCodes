# Code by @AmirMotefaker

# object-oriented Programming (OOPs)

# # Solution 1
# class Car:
#     def __init__(self, car_color):
#         self.color = car_color  # instance attribute

# car1 = Car('blue')  # instance
# car2 = Car('yellow')
# car3 = Car('red')   # instance

# print(car1.color)
# print(car2.color)

# # Output:
# # blue
# # yellow


# # Solution 2
# class Car:
#     def __init__(self, color, model):  # constructor
#         self.color = color  # instance attribute
#         self.model = model

# car1 = Car('blue', 'BMW')  # instance
# car2 = Car('yellow', 'AUDI')
# car3 = Car('red', 'BMW')   # instance

# print(car1.color)
# print(car1.model)
# print(car2.color)
# print(car2.model)

# # Output:
# # blue
# # BMW
# # yellow
# # AUDI


# # Solution 3
# class Car:
#     def __init__(self, color, model):  # constructor
#         self.color = color  
#         self.model = model

#     def print_details(self):
#         return f'color: {self.color} model: {self.model}'

# car1 = Car('blue', 'BMW') 

# print(car1.print_details())

# # Output:
# # color: blue model: BMW


# # Solution 4
# class Car:
#     def __init__(self, color, model):  # constructor
#         self.color = color  
#         self.model = model

#     def print_details(self):
#         return f'color: {self.color}, model: {self.model}'

# car1 = Car('blue', 'BMW')  
# car2 = Car('yellow', 'AUDI')
# car3 = Car('red', 'BMW')   # 

# print(car1.print_details())
# print(car2.print_details())
# print(car3.print_details())

# # Output:
# # color: blue, model: BMW
# # color: yellow, model: AUDI
# # color: red, model: BMW


# # Solution 5
# class Car:
#     def __init__(self, color, model):  # constructor
#         self.color = color  
#         self.model = model

#     def print_details(self):
#         return f'color: {self.color}, model: {self.model}'

# car1 = Car('blue', 'BMW')  
# print(car1.color, car1.model)
# print(car1.print_details())

# # Output:
# # blue BMW
# # color: blue, model: BMW


# Solution 6 - self
class Car:
    def __init__(self, color, model):  # constructor
        self.color = color  
        self.model = model

    def print_details(self, a):
        return f'color: {self.color}, model: {self.model} {a}'


car1 = Car('blue', 'BMW')  
print(car1.print_details(20))
print(Car.print_details(car1, 20))

# Output:
# color: blue, model: BMW 20
# color: blue, model: BMW 20
