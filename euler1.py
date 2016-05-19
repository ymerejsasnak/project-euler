# sum of all multiples of 3 and 5 below 1000

# basic formula for sum of numbers from 1 to n
def summation(n):
    return n / 2 * (n + 1)

# summation of multiples  ('c' being the constant 'multiplier' 
# and 'n // c' being the highest multiple of c below n)
def sum_multiples(c, n):
    return summation(n // c) * c
    

# get sums (going up to 999 since it says 'below 1000')
sum_threes = sum_multiples(3, 999)
sum_fives = sum_multiples(5, 999)

# then get multiples of 15 to subtract from above since they'd be counted twice
sum_fifteens = sum_multiples(15, 999)

print(sum_threes + sum_fives - sum_fifteens)
