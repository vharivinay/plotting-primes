'''
This fun project and playing with primes was insprired by 3Blue1Brown's video on youtube.

3Blue1Brown is a brilliant youtube channel on mathematics
Here is the link for the video: https://www.youtube.com/watch?v=EK32jo7i5LQ

This code replicates the distribution of prime numbers plot in a polar co-ordinate system seen in the video.
You can plot the first n prime numbers. Here there is only one input defined by the variable num.

'''

import math
import matplotlib.pyplot as plt
import numpy as np
from numba import jit
import time

@jit(nopython=True)
def is_prime(num):
    '''
    This function checks if any number is a prime number
    '''
    if num < 2:
        return False
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


@jit(nopython=True)
def nth_prime(n):
    '''
    This function generates the first n prime number where is defined by the user.
    n can change by assigning any positive integer to the variable num below
    '''
    i = 1
    j = 0
    list_of_primes = []
    while j < n:
        if is_prime(i):
            list_of_primes.append(i)
            j += 1
        i += 1
        #print(j, end='\r')
    return list_of_primes


## Running the functions here
num = 100000 ##-----> INPUT HERE

tic = time.perf_counter()
primes = nth_prime(num)
toc = time.perf_counter()

time = abs(toc - tic)

print('\n',time)
n = len(primes)

## Visualization
f = plt.figure(figsize=(10,10))
plt.subplot(111,polar = True)
ax1 = plt.scatter(primes,primes, s = 0.05)
plt.title(str(n)+' Primes', fontsize=36)
plt.axis('off')
plt.show()

f.savefig('{}_primes.png'.format(num),format='PNG',dpi=800)