# Code by @AmirMotefaker

# Find All File with .txt Extension Present Inside a Directory

# Solution 1 - Using glob
import glob, os

os.chdir("mydir")
for file in glob.glob("*.txt"):
    print(file)

# Output:
# a.txt
# b.txt
# c.txt



# Solution 2 - Using os
import os

for file in os.listdir("mydir"):
    if file.endswith(".txt"):
        print(os.path.join("mydir", file))


# Output:
# mydir\a.txt
# mydir\b.txt
# mydir\c.txt



# Solution 3 - Using os.walk
import os

for root, dirs, files in os.walk("mydir"):
    for file in files:
        if file.endswith(".txt"):
            print(file)


# Output:
# a.txt
# b.txt
# c.txt
