# Plotting Primes

## This fun project and playing with primes was insprired by 3Blue1Brown's video on youtube.

**3Blue1Brown is a brilliant youtube channel on mathematics
Here is the link for the video: https://www.youtube.com/watch?v=EK32jo7i5LQ**

**This code replicates the distribution of prime numbers plot in a polar co-ordinate system seen in the video.
You can plot the first n prime numbers. Here there is only one input defined by the variable num.**

**These codes run much faster on GPU using namba library.
- install numba if you want using 'pip install numba'

## How to
*  biggestPrime.py - computes the biggest primefactor of a given number. (No link to the plots.)
*  Nth_Prime.py - Generates the n (input) no. of primes and renders the plots seen below. Change num to any desired number.
  -  Comment out the decorator @jit(nopython=True) if you dont have a cuda supported gpu or numba installted
  

## Plots
<img width="500px" height="500px" src="1e3.png">
<img width="500px" height="500px" src="10e4.png">
