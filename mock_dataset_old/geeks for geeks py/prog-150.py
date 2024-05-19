from itertools import product
  
# Initializing list
test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
  
# printing original list
print("The original list is : " + str(test_list))
  
# Pair elements with Rear element in Matrix Row
# using product() + loop
res = []
for idx in test_list:
    res.append(list(product(idx[:-1], [idx[-1]])))
      
# printing result 
print ("The list after pairing is : " + str(res))