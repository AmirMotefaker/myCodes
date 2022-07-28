# Code by @AmirMotefaker

# RegEx - 

# # Solution 1 - Search the string
# import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

# # Output:
# # <re.Match object; span=(0, 17), match='The rain in Spain'>



# # Solution 2 - findall() Function
# import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

# Output:
# ['ai', 'ai']



# Solution 3 - search() Function
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# Output:
# The first white-space character is located in position: 3

