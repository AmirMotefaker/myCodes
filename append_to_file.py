# Code by AmirMotefaker

# Append to a File

# my_file.txt:
# honda 1948
# mercedes 1926
# ford 1903

with open("my_file.txt", "a") as f:
   f.write("new text")

# output:
# change my_file.txt:
# honda 1948
# mercedes 1926
# ford 1903new text
