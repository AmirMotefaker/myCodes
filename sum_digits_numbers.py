# Code by @AmirMotefaker

# Calculate the sum of digits of numbers

# 1234 -> 10

# 1234 % 10 -> 4
# 1234 // 10 -> 123
# 123 % 10 -> 3
# 123 // 10 -> 12
# 12 % 10 -> 2
# 12 // 10 -> 1
# 1 % 10 -> 1
# 1 // 10 -> 0

user_input = int(input('Enter your number: '))

result = 0

while user_input != 0:
    result += user_input % 10
    user_input = user_input // 10

print(result)

# Output:
# Enter your number: 1234
# 10

# Output:
# Enter your number: 99991
# 37
