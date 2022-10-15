# Code by @AmirMotefaker

# Get Line Count of a File

# Solution 1 - Using a for loop
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(file_len("my_file.txt"))

# Output:
# 3



# Solution 2 - Using list comprehension
num_of_lines = sum(1 for l in open('my_file.txt'))

print(num_of_lines)

# Output:
# 3
