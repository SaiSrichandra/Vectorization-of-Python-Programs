from functools import reduce
list1 = [1, 2, 3]
list2 = [3, 2, 4]
 
 
result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)