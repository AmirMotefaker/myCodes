# Code by amotef@gmail.com

# projecteuler.net
# ID 4

# Largest Palindrome Product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Prime Factor: any of the prime numbers that can be multiplied to give the original number.
# Example: The prime factors of 15 are 3 and 5 (because 3×5=15, and 3 and 5 are prime numbers).

    
def larrgestPalindrome(n):
 
    upper_limit = (10**(n))-1  # largest number of n-1 digit.
    lower_limit = 1 + upper_limit//10   # One plus this number is lower limit which is product of two numbers.
  
    max_product = 0 # Initialize result
    for i in range(upper_limit,lower_limit-1, -1):
     
        for j in range(i,lower_limit-1,-1):
         
            # calculating product of
            # two n-digit numbers
            product = i * j
            if (product < max_product):
                break
            number = product
            reverse = 0
  
            # calculating reverse of
            # product to check
            # whether it is palindrome or not
            while (number != 0):
             
                reverse = reverse * 10 + number % 10
                number =number // 10
             
  
             # update new product if exist and if
             # greater than previous one
            if (product == reverse and product > max_product):
                max_product = product
         
     
    return max_product
 
# Driver code
 
n1 = 2
n2 = 3
print('Largest palindrome product', n1, '- digit is: ', larrgestPalindrome(n1))
print('Largest palindrome product', n2, '- digit is: ', larrgestPalindrome(n2))
