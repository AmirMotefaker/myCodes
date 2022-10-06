# Code by @AmirMotefaker

# Count the Number of Digits Present In a Number

# Solution 1 - Count Number of Digits in an Integer using while loop
num = 3452
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))

# Output:
# Number of digits: 4



# Solution 2 - Using inbuilt methods
num = 123456
print(len(str(num)))


# Output:
# 6
