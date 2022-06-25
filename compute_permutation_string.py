# Code by @AmirMotefaker

# Compute all the Permutation of the String

# Solution 1 - Using recursion
def get_permutation(string, i=0):

    if i == len(string):   	 
        print("".join(string))

    for j in range(i, len(string)):

        words = [c for c in string]
   
        # swap
        words[i], words[j] = words[j], words[i]
   	 
        get_permutation(words, i + 1)

print(get_permutation('amir'))

# Output:
# amir
# amri
# aimr
# airm
# arim
# armi
# mair
# mari
# miar
# mira
# mria
# mrai
# imar
# imra
# iamr
# iarm
# iram
# irma
# rmia
# rmai
# rima
# riam
# raim
# rami
# None
