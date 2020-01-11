from itertools import count, islice, accumulate
from functools import reduce
import time

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def find_n(nfactors, n):
    # There should be some better searching algo here ;)
    return n + 1

def generator_triangle_value(n):
    return (1 + n) / 2 * n

start = time.time()

n = 10
tri_val = generator_triangle_value(n)
nfactors = len(factors(tri_val))

while nfactors <= 500:
    n = find_n(nfactors, n)
    tri_val = generator_triangle_value(n)
    nfactors = len(factors(tri_val))

elapsed = (time.time() - start)
print(f'elapsed time: {elapsed}')
print(f'1st triangle value with >500 factors is: {tri_val}')
# elapsed time: 6.851911783218384
# 1st triangle value with >500 factors is: 76576500.0



# a quicker solution
from itertools import count, islice, accumulate
from functools import reduce
import numba


def divisors(n): 
    step = 2 if n%2 else 1
    return set(reduce( list.__add__, ([i, n//i] for i in islice(count(1),  0, int(n**0.5) + 1, step) if n%i==0)))


start = time.time()
for i in islice(accumulate(count(1)), 0, None):
    if len(divisors(i)) > 500:
        print(i)
        break

elapsed = (time.time() - start)
print(f'elapsed time: {elapsed}')

#76576500
#elapsed time: 2.8360092639923096


# an even quicker solution using numba
@numba.jit(nopython=True)
def divisors_numba(n): 
    c = 0
    step = 1
    for i in range(1, int(n**0.5) + 1, step):
        if n%i == 0:
            c += 1
        if c > 500 / 2:
            return c * 2 
    return c * 2  

start = time.time()
for i in islice(accumulate(count(1)), 0, None):
    if divisors_numba(i) > 500:
        print(i)
        break

elapsed = (time.time() - start)
print(f'elapsed time: {elapsed}')
# 76576500
# elapsed time: 0.30629849433898926

# one way to speed it up is to consider only triangle number with 2, 3, 5, 7 
# as prime factors (this list can be extended but not too long ;)
  