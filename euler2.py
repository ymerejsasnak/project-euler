# By considering the terms in the Fibonacci sequence whose values do not exceed 
# four million, find the sum of the even-valued terms.


# create a list and store fibonacci sequence, stopping before 
# final value is greater than n
# (lazy code will always output [1, 2] even for n values below 2)
def fib_list(n):
    fib = [1, 2]
    while fib[-1] + fib[-2] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

# use above to get sequence and use comprehension to only keep even values
even_fibs = [x for x in fib_list(4000000) if x % 2 == 0]

# print the sum of these values
print(sum(even_fibs))


# likely not the best way to do it, but it works
    
