# Code by AmirMotefaker

# Convert Celsius To Fahrenheit and Fahrenheit to Celsius

# Python Program to convert temperature in celsius to fahrenheit

# Solution 1
# change this value for a different result
# celsius = float(input("Enter value in celsius: "))

# # calculate fahrenheit
# fahrenheit = (celsius * 1.8) + 32
# print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

# Output:
# Enter value in celsius: 45
# 45.0 degree Celsius is equal to 113.0 degree Fahrenheit



# Solution 2 - CodingYar
# celsius To fahrenheit
# f = (c * 1.8) + 32
def celsius_to_fahrenheit(celsius):
    num1 = celsius * 1.8
    return num1 + 32



# c = (f - 32) / 1.8
def fahrenheit_to_celsius(fahrenheit):
    num1 = (fahrenheit - 32)
    return num1 / 1.8


print(celsius_to_fahrenheit(45))
# Output:
# 113.0

print(fahrenheit_to_celsius(113)) 
# Output:
# 45.0

