# Code by @AmirMotefaker

#  Check If Two Strings are Anagram

# str1 = "Race"
# str2 = "Care"

# # convert both the strings into lowercase
# str1 = str1.lower()
# str2 = str2.lower()

# # check if length is same
# if(len(str1) == len(str2)):

#     # sort the strings
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)

#     # if sorted char arrays are same
#     if(sorted_str1 == sorted_str2):
#         print(str1 + " and " + str2 + " are anagram.")
#     else:
#         print(str1 + " and " + str2 + " are not anagram.")

# else:
#     print(str1 + " and " + str2 + " are not anagram.")


# # Output:
# # race and care are anagram.



# Solution 2
NO_OF_CHARS = 256
 
# function to check if two strings
# are anagrams of each other
def areAnagram(str1,str2):
     
    # If both strings are of different
    # length. Removing this condition
    # will make the program fail for
    # strings like "aaca" and "aca"   
    if(len(str1) != len(str2)):
        return False;
       
    # Create a count array and initialize
    # all values as 0
    count=[0 for i in range(NO_OF_CHARS)]
    i=0
     
    # For each character in input strings,
    # increment count in the corresponding
    # count array
    for i in range(len(str1)):
        count[ord(str1[i]) - ord('a')] += 1;
        count[ord(str2[i]) - ord('a')] -= 1;
         
    # See if there is any non-zero
    # value in count array
    for i in range(NO_OF_CHARS):
        if (count[i] != 0):
            return False
         
     
    return True
 
# Driver code
str1="listen"
str2="silent"
 
# Function call
if (areAnagram(str1, str2)):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")
     
     
# This code is contributed by patel2127

# Output:
# The two strings are anagram of each other
