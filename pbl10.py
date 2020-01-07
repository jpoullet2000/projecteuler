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
        primes_to_check = [prime for prime in primes if prime < num/2]
        for i in primes_to_check: 
            if (num % i) == 0:
                prime = False
                break
        if prime:
            primes.append(num)
    return primes


max_nr = 100000 #2_000_000
start_time = time.time()
primes = get_primes(max_nr)
print(f'The number of primes is {len(primes)}')
print(f'The sum of primes is {sum(primes)}')
stop_time = time.time()
time_spent = stop_time - start_time
print(f'Time spent: {time_spent}')

# Answer: 
# The number of primes is 148933
# The sum of primes is 142913828922
# Time spent: 1402.0321731567383

# For max_nr = 100_000 it only takes 5s. In that case we have
# The number of primes is 9592
# The sum of primes is 454396537
# Time spent: 5.078207969665527
# FYI, without numba it takes 7x more time: Time spent: 35.02199864387512