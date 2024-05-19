test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
  
# printing original list 
print("The original list : " + str(test_list))
  
# initialize add element
add_ele = 4
  
# Update each element in tuple list
# Using list comprehension + map() + lambda
res = [tuple(map(lambda ele : ele + add_ele, sub)) for sub in test_list]
  
# printing result
print("List after bulk update : " + str(res))