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


# # Solution 6 - self
# class Car:
#     def __init__(self, color, model):  # constructor
#         self.color = color  
#         self.model = model

#     def print_details(self, a):
#         return f'color: {self.color}, model: {self.model} {a}'


# car1 = Car('blue', 'BMW')  
# print(car1.print_details(20))
# print(Car.print_details(car1, 20))

# # Output:
# # color: blue, model: BMW 20
# # color: blue, model: BMW 20



# # Solution 7 - Instance Attributes and Class Attributes
# class House:
#     def __init__(self, color, num_of_rooms, a):
#         self.color = color
#         self.num_of_rooms = num_of_rooms
#         self.a = a

# house1 = House('blue', 4, 100)

# print(house1.color)
# print(house1.a)

# # Output:
# # blue
# # 100


# # Solution 8 - Instance Attributes and Class Attributes
# class House:
#     def __init__(self, color, num_of_rooms, a):
#         self.color = color
#         self.num_of_rooms = num_of_rooms
#         self.a = a

#     def house_description(self):
#         return (self.color, self.num_of_rooms, self.a)

# house1 = House('blue', 4, 100)
# john_house = House('yellow', 3, 150)

# # print(house1.color)
# # print(house1.a)
# print(house1.house_description())

# # print(john_house.color)

# # Output:
# # ('blue', 4, 100)



# # Solution 9 - Instance Attributes and Class Attributes
# class House:
#     country = 'iran'  # Class Attributes

#     def __init__(self, color, num_of_rooms, a):
#         self.color = color
#         self.num_of_rooms = num_of_rooms
#         self.a = a

#     def house_description(self):
#         return (self.color, self.num_of_rooms, self.a)

# house1 = House('blue', 4, 100)
# house1.color = 'black'
# john_house = House('yellow', 3, 150)

# print(house1.color)
# print(house1.country)
# print(john_house.country)

# # Output:
# # black
# # iran
# # iran



# # Solution 10 - Instance Attributes and Class Attributes
# class House:
#     country = 'iran'  # Class Attributes

#     def __init__(self, color, num_of_rooms, a):
#         self.color = color
#         self.num_of_rooms = num_of_rooms
#         self.a = a

#     def house_description(self):
#         return (self.color, self.num_of_rooms, self.a)

# house1 = House('blue', 4, 100)
# house1.country = 'USA'   # Instance Attributes
# house1.color = 'black'

# print(house1.country)

# # Output:
# # USA


# # Solution 11 - Instance Attributes and Class Attributes
# class House:
#     country = 'iran'  # Class Attributes

#     def __init__(self, color, num_of_rooms, a):
#         self.color = color
#         self.num_of_rooms = num_of_rooms
#         self.a = a

#     def house_description(self):
#         return (self.color, self.num_of_rooms, self.a)

# house1 = House('blue', 4, 100)
# print(house1.color)
# del house1.color
# print(house1.color)


# # Output:
# # blue
# # Traceback (most recent call last):
# #   File "e:\A.Motefaker\ABC\Python\MyCode\OOP_sample.py", line 227, in <module>
# #     print(house1.color)
# # AttributeError: 'House' object has no attribute 'color'


# Solution 12 - Instance Attributes and Class Attributes
class House:
    country = 'iran'  # Class Attributes
    x = 123
    def __init__(self, color, num_of_rooms, a):
        self.color = color
        self.num_of_rooms = num_of_rooms
        self.a = a

    def house_description(self):
        return (self.color, self.num_of_rooms, self.a)

house1 = House('blue', 4, 100)
print(house1.country)
house1.country = 'USA'  # Instance Attributes
print(house1.country)
del house1.country
print(house1.country)

# Output:
# iran
# USA
# iran
