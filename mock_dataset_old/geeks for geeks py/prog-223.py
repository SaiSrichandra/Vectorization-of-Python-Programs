test_list = [(4, ), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]
  
# printing original list
print("The original list is : " + str(test_list))
  
# Initializing desired lengths 
i, j = 2, 3
  
# Filter Range Length Tuples
# Using filter() + lambda + len()
res = list(filter(lambda ele: len(ele) >= i and len(ele) <= j, test_list))
      
# printing result
print("The tuple list after filtering range records : " + str(res))