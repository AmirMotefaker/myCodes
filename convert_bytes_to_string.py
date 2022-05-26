# Code by @AmirMotefaker

# Convert Bytes to a String

# Using decode(), you can convert bytes into string.
# Here, we have used utf-8 for decoding.
# \xE2\x9C\x85 is the utf-8 code for ✅.

print(b'Amir Motefaker \xE2\x9C\x85'.decode("utf-8"))
