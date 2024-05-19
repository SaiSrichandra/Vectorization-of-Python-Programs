# Python3 code to demonstrate working of
# Convert tuple to List with succeeding element
# Using chain.from_iterable() + list() + generator expression
from itertools import chain

# initializing tuple
test_tup = (5, 6, 7, 4, 9)

# printing original tuple
print("The original tuple is : ", test_tup)

# initializing K
K = "Gfg"

# list comprehension for nested loop for flatten
res = list(chain.from_iterable((ele, K) for ele in test_tup))

# printing result
print("Converted Tuple with K : ", res)