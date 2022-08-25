# Code by @AmirMotefaker

# String Encryption and Decryption


# String Encryption
my_string = input('Enter string: ')

nums = []

for char in my_string:
    nums.append(str(ord(char) + 12))

secret_string = ','.join(nums)
print(secret_string)

# secret_string = '84,113,120,120,123,58,44,89,133,44,122,109,121,113,44,117,127,44,84,109,112,117,58'


# String Decryption
string_list = []

for num_str in secret_string.split(','):
    string_list.append(chr(int(num_str)-12))

print(''.join(string_list))

