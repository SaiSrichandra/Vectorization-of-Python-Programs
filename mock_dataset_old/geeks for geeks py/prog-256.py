# Python3 code to demonstrate working of
# Summation combination in tuple lists
# Using list comprehension + zip() + operator.add + combinations()
from itertools import combinations
import operator

# initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10)]

# printing original list
print("The original list : " + str(test_list))

# Summation combination in tuple lists
# Using list comprehension + zip() + operator.add + combinations()
res = [(operator.add(*a), operator.add(*b))\
	for a, b in (zip(y, x) for x, y in combinations(test_list, 2))]

# printing result
print("The Summation combinations are : " + str(res))