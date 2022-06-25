# Code by @AmirMotefaker

# Count the Number of Occurrence of a Character in String

# Solution 1 - Using a for loop
count = 0

my_string = "amir motefaker"
my_char = "a"

for i in my_string:
    if i == my_char:
        count += 1

print(count)

# Output:
# 2
