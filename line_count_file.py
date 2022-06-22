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

