'''
2520 is the smallest number that can be divided by each of 
the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?
'''
# good solution probably involves some trickery with the primes in 1-20
# but after lots of thought and playing with numbers, couldn't get it quite right
# so brute force:


n = 2520 # number must be a multiple of this (as given above), since 1-10 are already factors too

# check only necessary factors: the primes above 10, but also 16 (which I'm guessing
# has something to do with it being a perfect square, so it's not actually the product
# of two of the numbers in 1-10, it's the square of ONE of them) --- and this is likely
# what tripped me up with trying a more intelligent/elegant solution.......anyway...

while n % 19 != 0 or n % 17 != 0 or n % 16 != 0 or n % 13 != 0 or n % 11 != 0:
    n += 2520

print(n)
