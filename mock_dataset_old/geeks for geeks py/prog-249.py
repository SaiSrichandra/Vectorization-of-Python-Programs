# Python3 code to demonstrate working of
# Flatten tuple of List to tuple
# Using tuple() + chain.from_iterable()
from itertools import chain

# initializing tuple
test_tuple = ([5, 6], [6, 7, 8, 9], [3])

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Flatten tuple of List to tuple
# Using tuple() + chain.from_iterable()
res = tuple(chain.from_iterable(test_tuple))

# printing result
print("The flattened tuple : " + str(res))