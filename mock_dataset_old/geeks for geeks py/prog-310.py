# Python3 code to demonstrate working of
# Elementwise AND in tuples
# using map() + iand
from operator import iand

# initialize tuples
test_tup1 = (10, 4, 6, 9)
test_tup2 = (5, 2, 3, 3)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Elementwise AND in tuples
# using map() + iand
res = tuple(map(iand, test_tup1, test_tup2))

# printing result
print("The AND tuple : " + str(res))