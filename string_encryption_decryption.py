# Code by @AmirMotefaker

# String Encryption and Decryption

# String Encryption
my_string = 'Hello. My name is Hadi.'

nums = []

for char in my_string:
    nums.append(str(ord(char) + 12))

print(','.join(nums))


secret_string = '84,113,120,120,123,58,44,89,133,44,122,109,121,113,44,117,127,44,84,109,112,117,58'

