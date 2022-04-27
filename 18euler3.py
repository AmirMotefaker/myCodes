# Code by amotef@gmail.com

# projecteuler.net
# ID 3

# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def findLargestPrimeFactor(n):
  primeFactor = 1
  i = 2

  while i <= n / i:
    if n % i == 0:
      primeFactor = i
      n /= i
    else:
      i += 1

  if primeFactor < n: primeFactor = int(n)

  return primeFactor

print("Largest prime factor 13195 is: ", findLargestPrimeFactor(13195))
print("Largest prime factor 600851475143 is: ", findLargestPrimeFactor(600851475143))
