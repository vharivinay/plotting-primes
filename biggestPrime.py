'''
=====> The function is_prime(num) checks if an input number is a prime number.
=====> The function pirmeFactors(num) computes the prime factors of a given number.

Test number: 600851475143 ---> Required for project euler question 3.

Author: Harivinay V
Github: https://github.com/M87K452b
'''

import math
from numba import jit

@jit(nopython=True)
def is_prime(num):
    '''
    Function: To check if a number is prime
    '''
    if num < 2:
        return False
    if num % 2 == 0 and num > 2: 
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

primes = []
factors = []

def primeFactors(num):
    '''
    Function to compute the primefactors of a given number
    '''
    i = 1
    while (num > 2 and i <= num):
        if is_prime(num):
            factors.append(num)
            break
        if is_prime(i):
            if num%i == 0:
                factors.append(i)
                num = num/i
                print(num,'|',i)
        i += 1
    return max(factors)

num=600851475143
largest_primeFactor = primeFactors(num)
print('The largest prime factor of {} is {}'.format(num,largest_primeFactor))



