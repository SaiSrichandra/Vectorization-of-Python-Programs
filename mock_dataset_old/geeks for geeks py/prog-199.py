test_tup = ([7, 8], [9, 1], [10, 7]) 
  
# printing original tuple
print("The original tuple is : " + str(test_tup)) 
  
# Tuple elements inversions
# Using map() + list() + sum()
res = sum(list(map(sum, list(test_tup))))
  
# printing result 
print("The summation of tuple elements are : " + str(res))