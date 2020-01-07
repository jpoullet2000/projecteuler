# Summation of primes
# One just needs to test if the modulo of the smaller primes is 0 
# 2 being the smallest prime, no need to calculate the modulo for primes > num / 2 
# (no need to test all numbers)
import numba
import time

@numba.jit(nopython=True)
def get_primes(max_nr):
    primes = [2, 3]
    for num in range(5, max_nr):
        prime = True
        for i in primes:
            if (num % i) == 0:
                prime = False
                break
        if prime:
            primes.append(num)
    return primes


max_nr = 2_000_000
start_time = time.time()
primes = get_primes(max_nr)
print(f'The number of primes is {len(primes)}')
print(f'The sum of primes is {sum(primes)}')
stop_time = time.time()
time_spent = stop_time - start_time
print(f'Time spent: {time_spent}')

# Answer: 
#The number of primes is 148933
#The sum of primes is 142913828922
#Time spent: 39.52696514129639

# For max_nr = 100_000 it takes less than 1s. In that case we have
# The number of primes is 9592
# The sum of primes is 454396537
# Time spent: 0.287992000579834
# FYI, without numba it takes 7-10x more time: Time spent: 2.1709048748016357