# Code by @AmirMotefaker

# String Encryption and Decryption


# # String Encryption
my_string = input('Enter string: ')

nums = []

for char in my_string:
    nums.append(str(ord(char) + 12))

secret_string = ','.join(nums)
print(secret_string)

# # Output:
# # Enter string: I am Amir.
# # 85,44,109,121,44,77,121,117,126,58



# String Decryption
string_list = []
secret_string = '85,44,109,121,44,77,121,117,126,58'

for num_str in secret_string.split(','):
    string_list.append(chr(int(num_str)-12))

print(''.join(string_list))

# Output:
# I am Amir.
