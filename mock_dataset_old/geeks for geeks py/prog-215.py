test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]
  
# printing original list
print("The original list is : " + str(test_list))
  
# filter() + lambda to drive logic of discarding tuples
res = list(filter(lambda sub : not all(ele == None for ele in sub), test_list))
  
# printing result 
print("Removed None Tuples : " + str(res))