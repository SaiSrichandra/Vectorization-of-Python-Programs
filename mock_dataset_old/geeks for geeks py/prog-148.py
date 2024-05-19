test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]
  
# printing original list
print ("The original list is : " + str(test_list))
  
# Reverse Row sort in Lists of List
# using list comprehension + sorted()
res = [sorted(sub, reverse = True) for sub in test_list]
  
# printing result 
print ("The reverse sorted Matrix is : " + str(res))