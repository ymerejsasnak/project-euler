'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


# given the two equalities above:  a + b + sqrt(a**2 + b**2) = 1000
# (cut out c so don't have to iterate through 3 variables, just 2)
# also don't forget a < b < c


# loop thru possible values of a
for a in range(1, 999):
    
    # loop thru possible values of b (starting at a since > a)
    for b in range(a + 1, 1000):
        
        # plug a and b into equation and when right ones found print product
        if a + b + (a**2 + b**2) ** (1/2) == 1000:
            print(str(a * b * (a**2 + b**2) ** (1/2)))
            
            
# there should be a way to cut down the range instead of going all the way 
# to 998/999, but I can't think of what it would be...






