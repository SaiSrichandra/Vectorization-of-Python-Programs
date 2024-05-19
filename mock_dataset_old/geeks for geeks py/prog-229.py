test_tup = (1, 4, 5, 6)
  
# printing original tuple 
print("The original tuple is : " + str(test_tup))
  
# Test if tuple is distinct
# Using set() + len()
res = len(set(test_tup)) == len(test_tup)
  
# printing result
print("Is tuple distinct ? : " + str(res))