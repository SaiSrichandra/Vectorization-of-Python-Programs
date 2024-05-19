from collections import OrderedDict
 
# Initializing tuple
test_tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
# Remove duplicate lists in tuples(Preserving Order)
# Using OrderedDict() + tuple()
res = list(OrderedDict((tuple(x), x) for x in test_tup).values())
 
# printing result
print("The unique lists tuple is : " + str(res))