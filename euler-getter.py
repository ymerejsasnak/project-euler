'''
quick and dirty program to get text of a euler problem
and put it into a docstring in an empty appropriately named file
'''


import requests
import sys


problem_number = sys.argv[1]  # will only take a number, anything else dropped, nothing checked currently
print(sys.argv, problem_number)


r = requests.get('https://projecteuler.net/problem=' + str(problem_number))

# split on unique bit of text before problem text, and only keep second half
problem_text = r.text.split('<div class="problem_content" role="problem">')[1]

# do the same, split on the div closing tag and only keep what comes before
problem_text = problem_text.split('</div>')[0]

problem_text = problem_text.replace('<p>', '').replace('</p>', '')

print(problem_number, problem_text)

