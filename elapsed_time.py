# Code by @AmirMotefaker

# Measure the Elapsed Time

## Solution 1

# Save the timestamp at the beginning of the code start using time().
# Save the timestamp at the end of the code end.
# Find the difference between the end and start, which gives the execution time.

# import time

# start = time.time()

# print(22*1.4)

# end = time.time()
# print(end - start)



## Solution 2


from timeit import default_timer as timer
# timeit provides the most accurate results.

start = timer()

print(22*1.4)

end = timer()
print(end - start)

