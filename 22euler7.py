# Code by amotef@gmail.com

# projecteuler.net
# Problem 7

# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

# A prime sieve or prime number sieve is a fast type of algorithm for finding primes.


# Algorithm: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# The sieve of Eratosthenes can be expressed in pseudocode:
# algorithm Sieve of Eratosthenes is
#     input: an integer n > 1.
#     output: all prime numbers from 2 through n.

#     let A be an array of Boolean values, indexed by integers 2 to n,
#     initially all set to true.
    
#     for i = 2, 3, 4, ..., not exceeding √n do
#         if A[i] is true
#             for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
#                 set A[j] := false

#     return all i such that A[i] is true.



import time, math

start = time.time()   #Time at the start of program execution

def Sieve_of_Eratosthenes(n):  # Sieve of Eratosthenes: method for finding all primes up to (and possibly including) a given natural n.
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
    
	for i in range(2,int(math.sqrt(n)+1)):   # Checking up to sqrt(n) is better than checking up to n.
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime

nth_prime = 10001   # the 10001st prime number

Maximum_bound = nth_prime*math.log(nth_prime) + nth_prime*math.log(math.log(nth_prime))   # nlogn+n(loglogn−1)<prime_number<nlogn+nlognlogn

print ("the 10001st prime number is:", Sieve_of_Eratosthenes(int(Maximum_bound))[10000])

end_time = time.time()   #Time at the end of execution

print ("Time of program execution:", (end_time - start))   # Time of program execution
