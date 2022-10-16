# Code by AmirMotefaker

# Message Encode - Decode

# # Solution 1 - basic
def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string

def decode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string


e = encode('Amir', 'Motefaker')
d = decode('Amir', e)
print([e])
print([d])

# # Output:
# # ['\x8eÜÝ×§ÎÔ×³']
# # ['Motefaker']



# # Solution 2 - advanced

import six, base64
# six: Provides simple utilities for wrapping over differences between Python 2 and Python 3.
# base64: This module provides functions for encoding binary data to printable ASCII characters and decoding such encodings back to binary data.

def encode(key, string):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    encoded_string = encoded_string.encode('latin') if six.PY3 else encoded_string
    return base64.urlsafe_b64encode(encoded_string).rstrip(b'=')

def decode(key, string):
    string = base64.urlsafe_b64decode(string + b'===')
    string = string.decode('latin') if six.PY3 else string
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string

e = encode('Amir', 'Motefaker')
d = decode('Amir', e)
print([e])
print([d])

# # Output:
# # [b'jtzd16fO1Nez']
# # ['Motefaker']



# # Solution 3 - advanced++

def encode_decode(key, string, act='e'):
   
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        if act=='e':
            encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        else:
            encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string

# use (key:Amir ,text:Motefaker) for encoding and (key,text, 'd') for decoding
e = encode_decode('Amir', 'Motefaker')
d = encode_decode('Amir', e,'d')
print(e)
print(d)

# Output:
# ÜÝ×§ÎÔ×³
# Motefaker
