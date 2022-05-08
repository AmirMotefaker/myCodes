# CodeWithMosh

# print ("Hello World")

# age = 20
# price = 19.95
# first_name = "Amir"
# is_online = True
# print (age, price, first_name , is_online)

# name = input ("What is your name? ")
# print ("Hello " + name)

# /3 Types of Data in Python
# /Numbers = 10  int()  float()
# /String = "Amir"   str()
# /Bolean = False, True   bool()
# birth_year = input("Enter your birth year: ")
# age = 2022 - int(birth_year)
# print(age)

# Exercise02
# first_number = input("Enter First Number: ")
# second_number = input("Enter Second Number: ")
# sum = float(first_number) + float(second_number)
# print("Sum", first_number, "+", second_number , " = ", sum)
# Exercise02-2
# first_number = float(input("Enter First Number: "))
# second_number = float(input("Enter Second Number: "))
# sum = first_number + second_number
# print("Sum", first_number, "+", second_number , " = ", sum)

# course = 'Python for Beginners'
# print('Python' in course)
# print(course.find('Python'))
# print(course.replace('for', '4'))
# print(course.find('Y'))
# print(course.upper())
# print(course)
# print(course.lower())

# print(10 + 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# x = 10
# x = x + 3 : x += 3
# x = x * 3 : x *= 3
# x = x - 3 : x -= 3

# x = (10 + 3) * 2
# print(x)

# x = 3 > 2
# print(x)
# x = 3 < 2
# print(x)
# x = 3 == 2
# print(x)
# x = 3 != 2
# print(x)

# price = 25
# print(price > 10 and price < 30)

# price = 5
# print(price > 10)
# print(not price > 10)

# if Statement
# temperature = 15
# if temperature > 30:
#     print("It's a hot day.")
#     print("Drink plenty of water")
# elif temperature > 20: # (20, 30]
#     print("It's a nice day")
# elif temperature > 10:  # (10, 20]
#     print("It's a bit cold")
# else:
#     print("It's cold")
# print("Done")

# Exercise03
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))
    
# i = 1
# while i <= 10:
#     print(i * '*')
#     i = i + 1


# List
# names = ["John", "Bob", "Mosh", "Sam", "Mary"]
# names[0] = "Jon"
# print(names[0:3])
# print(names)
# print(names[0])
# print(names[-1])

# List Methods
# numbers = [1, 2, 3, 4, 5]
# numbers.clear()
# numbers.remove(3)
# numbers.insert(0, -1)
# numbers.append(6)
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# print(1 in numbers)

# numbers = [1, 2, 3, 4, 5]
# print(len(numbers))


# For Loops
# numbers = [1, 2, 3, 4, 5]
# for items in numbers:
#     print(items)
#
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i = i + 1


# The range() Function
# numbers = range(5, 10, 2)
# for number in range(5):
# print(number)


# Tuples
# numbers = (1, 2, 3, 3)
# print(numbers.count(3))
