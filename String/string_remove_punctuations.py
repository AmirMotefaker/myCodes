# Code by @AmirMotefaker

# Remove Punctuations From a String

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# my_str = "Hello?!!!, he said --*-and went."
my_str = input("Enter a string: ")

no_punctuations = ""
for char in my_str:
   if char not in punctuations:
       no_punctuations = no_punctuations + char

print(no_punctuations)
