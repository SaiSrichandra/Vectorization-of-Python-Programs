from collections import Counter
from itertools import chain
  
# List initialization
Input = [[('hi', 'bye')], [('Geeks', 'forGeeks')],
         [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]
  
# Using counter and chain
Output = Counter(chain(*Input))
  
# Printing output
print(Output)