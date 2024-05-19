# Python3 code to demonstrate working of
# Cross Tuple AND operation
# using map() + iand()
import operator

# initialize tuples
test_tup1 = (10, 4, 5)
test_tup2 = (2, 5, 18)

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Cross Tuple AND operation
# using map() + iand()
res = tuple(map(operator.iand, test_tup1, test_tup2))

# printing result
print("Resultant tuple after AND operation : " + str(res))