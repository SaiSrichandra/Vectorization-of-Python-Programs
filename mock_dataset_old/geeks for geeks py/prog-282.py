# Python3 code to demonstrate working of
# Unique elements in nested tuple
# Using from_iterable() + set()
from itertools import chain

# initialize list
test_list = [(3, 4, 5), (4, 5, 7), (1, 4)]

# printing original list
print("The original list : " + str(test_list))

# Unique elements in nested tuple
# Using from_iterable() + set()
res = list(set(chain.from_iterable(test_list)))

# printing result
print("Unique elements in nested tuples are : " + str(res))