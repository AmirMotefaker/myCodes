# Code by @AmirMotefaker

# RegEx - 

# # Solution 1 - Search the string
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# # Output:
# # <re.Match object; span=(0, 17), match='The rain in Spain'>



# # Solution 2 - findall() Function
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# Output:
# ['ai', 'ai']



# # Solution 3 - search() Function
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# # Output:
# # The first white-space character is located in position: 3


# # Solution 4 - search() Function
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# # Output:
# # None



# # Solution 5 - split() Function
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# # Output:
# # ['The', 'rain', 'in', 'Spain']



# # Solution 6 - split() Function
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# # Output:
# # ['The', 'rain in Spain']


# # Solution 7 - sub() Function
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# # Output:
# # The9rain9in9Spain


# # Solution 8 - sub() Function
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# # Output:
# # The9rain9in Spain



# # Solution 9 - Match Object
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

# # Output:
# # <re.Match object; span=(5, 7), match='ai'>


# # Solution 10 - Match Object
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# # Output:
# # (12, 17)



# # Solution 11 - Match Object
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# # Output:
# # The rain in Spain


# Solution 12 - Match Object
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

# Output:
# Spain
