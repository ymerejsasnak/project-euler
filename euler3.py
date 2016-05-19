# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?



# basic seive of eratosthenes to generate primes <= n
def erato_seive(n):
    # first create list of all ints from 2 to n
    integers = list(range(2, n + 1))
    
    for p in range(2, n // 2 + 1):
        # make list of all multiples of 2,3,4,...,n/2 + 1 
        # (without the plus 1 had edge case error when n == 4 and 5)
        removals = list(range(p * 2, n + 1, p))
        # then remove those and loop back to do next increment of p
        integers = [x for x in integers if x not in removals]
            
    return integers
    
    
# WOW...after messing around above making a seive of eratosthenes to generate
# primes I realized it would be this simple:
# (keeping the above here for now to perhaps use in the future)


def largest_prime_factor(n):
    # start with 2...lowest possible prime factor
    factor = 2
    
    # loop until n has been reduced to 1 through factoring out #s
    while n != 1:
        
        # modulus to check if # is indeed a factor
        # loops to take care of multiples (ie if # is a multiple of 4 it will
        # factor out 2 twice before incrementing the 'factor' variable)
        while n % factor == 0:
            n = n // factor
        
        # then if we aren't done (n!=1), increment to next possible factor
        # runs naively through odd numbers rather than primes...because any
        # non-prime odds (ie 9) will already be factored out (ie 3 and 3)  [seive like?]
        if n != 1:
            if factor == 2:
                factor = 3
            else:
                factor += 2
    
    return factor




print(largest_prime_factor(600851475143))
