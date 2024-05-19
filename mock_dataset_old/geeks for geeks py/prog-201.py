from operator import mod
  
# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)
  
# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))
  
# Tuple modulo
# using map() + mod
res = tuple(map(mod, test_tup1, test_tup2))
  
# printing result
print("The modulus tuple : " + str(res))