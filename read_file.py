# Code by @AmirMotefaker

# Read a File Line by Line Into a List

# Solution 1 - Using readlines()
# with open("data_file.txt") as f:
#     content_list = f.readlines()

# # print the list
# print(content_list)

# # remove new line characters
# content_list = [x.strip() for x in content_list]
# print(content_list)


# Solution 2 - Using for loop and list comprehension
with open('data_file.txt') as f:
    content_list = [line for line in f]

print(content_list)

# removing the characters
with open('data_file.txt') as f:
    content_list = [line.rstrip() for line in f]

print(content_list)

