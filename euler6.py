'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
'''

# seems like brute force should be easy and quick so whatever....


def sum_of_sqrs(n):
    return sum([x ** 2 for x in range(n + 1)]) 
       
def sqr_of_sum(n):
    return sum([x for x in range(n + 1)]) ** 2


print(sqr_of_sum(100) - sum_of_sqrs(100))



