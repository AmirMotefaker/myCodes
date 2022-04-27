# Code by amotef@gmail.com

# projecteuler.net
# ID 3

# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Prime Factor: any of the prime numbers that can be multiplied to give the original number.
# Example: The prime factors of 15 are 3 and 5 (because 3×5=15, and 3 and 5 are prime numbers).


def FLPF(n): # FLPF: Find Largest Prime Factor
   primeFactor = 1 # A factor that is a prime number
   i = 2

   while i <= n / i:
     if n % i == 0:
       primeFactor = i
       n /= i
     else:
       i += 1

   if primeFactor < n: primeFactor = int(n)

   return primeFactor

print("Largest prime factor 13195 is: ", FLPF(13195))
print("Largest prime factor 600851475143 is: ", FLPF(600851475143))
