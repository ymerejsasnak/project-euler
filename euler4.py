'''A palindromic number reads the same both ways. The largest palindrome made
 from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''


'''
notes/thoughts:
-answer will be less than 998001 (999 * 999)
-answer will be more than 10000 (100 * 100)
-so answer will be somewhere between 10001 and 997799

-probably unrealistic to brute force this so look for patterns......


'''

#NEW: 
# WOW - did not realize below would be that simple 
# leaving it as is even though it could be changed to be more general purpose
# and to give actual answer rather than list of all palindromes

# OLD:
# function to help look for patterns, cycles through 100 to 999 for each factor
# saves them to list if palindromic

def create_pals(rmin, rmax):
    pals = []
    for i in range(rmin, rmax):
        for j in range(i, rmax): # use i as start of inner loop so as not to repeat factors unnecissarily
            product = i * j
            if str(product) == str(product)[::-1]:
                pals.append([product, i, j])
                pals.sort()
    
    return pals

print(create_pals(100, 1000))


