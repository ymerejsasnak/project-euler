'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

# brute force

def is_prime(n):
    # a factor of a number cannot be higher than its square root
    highest = int(n ** (1/2))
    
    # naively check all numbers sqrt and below to see if any are factors
    for factor in range(2, highest + 1):
        if n % factor == 0:
            return False
    
    # if no factors, it's a prime!
    return True


# generates a tuple of prime number and which prime number it is (ie 5th, 6th, etc)
def prime_gen():
    # first one hard coded so can just add 2 in loop to skip over even numbers
    yield 2, 1
        
    number = 3
    count = 1
    
    while True:
        if is_prime(number):
            count += 1
            yield number, count
        number += 2



p = prime_gen()
for i in range(10001):
    answer = next(p)


print(str(answer[1]) + ': ' + str(answer[0]))
    
    
    
    
