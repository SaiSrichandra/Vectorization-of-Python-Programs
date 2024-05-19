from collections import OrderedDict
  
# initialize tuple
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
  
# printing original tuple 
print("The original tuple is : " + str(test_tup))
  
# Removing duplicates from tuple 
# using OrderedDict() + fromkeys()
res = tuple(OrderedDict.fromkeys(test_tup).keys())
  
# printing result
print("The tuple after removing duplicates : " + str(res))