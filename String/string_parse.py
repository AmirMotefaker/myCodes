# Code by @AmirMotefaker

# Parse a String to a Float or Int

# Solution 1 - Parse string into integer
balance_str = "1500"
balance_int = int(balance_str)

# print the type
print(type(balance_int))
# <class 'int'>

# print the value
print(balance_int)
# 1500


# Solution 2 - Parse string into float
balance_str = "1500.4"
balance_float = float(balance_str)

# print the type
print(type(balance_float))
# <class 'float'>

# print the value
print(balance_float)
# 1500.4


# Solution 3 - A string float numeral into integer
balance_str = "1500.34"
balance_int = int(float(balance_str))

# print the type
print(type(balance_int))
# <class 'int'>

# print the value
print(balance_int)
# 1500
