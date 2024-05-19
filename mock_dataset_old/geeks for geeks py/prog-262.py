# Python3 code to demonstrate working of
# Convert Tuple Matrix to Tuple List
# Using chain.from_iterable() + zip()
from itertools import chain

# initializing list
test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]

# printing original list
print("The original list is : " + str(test_list))

# flattening using from_iterable
res = list(zip(*chain.from_iterable(test_list)))

# printing result
print("The converted tuple list : " + str(res))