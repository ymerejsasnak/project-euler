'''
quick and dirty program to get text of a euler problem
and put it into a docstring in an empty appropriately named file
'''


import requests
import sys
import os.path


problem_number = sys.argv[1]  # will only take a number, anything else dropped, nothing checked currently
print(sys.argv, problem_number)


r = requests.get('https://projecteuler.net/problem=' + problem_number)

# split on unique bit of text before problem text, and only keep second half
problem_text = r.text.split('<div class="problem_content" role="problem">')[1]

# do the same, split on the div closing tag and only keep what comes before
problem_text = problem_text.split('</div>')[0]

# remove paragraph tags
problem_text = problem_text.replace('<p>', '').replace('</p>', '')

# note some formatting tags (sup, sub, etc) will remain currently...but maybe that's ok for now
# other note:  add newlines every 80 characters or so?



filename = 'euler' + problem_number + '.py'

if os.path.isfile(filename):
    print('File already exists...exiting...')
else:
    with open(filename, 'w') as f:
        f.write("'''" + problem_text + "'''")
    print(filename + ' created.')

