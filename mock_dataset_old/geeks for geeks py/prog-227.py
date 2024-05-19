test_list = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initialize ele 
ele = 3
  
# initialize K 
K = 1
  
# Records with Value at K index
# Using enumerate() + list comprehension
res = [b for a, b in enumerate(test_list) if b[K] == ele]
  
# printing result
print("The tuples of element at Kth position : " + str(res))