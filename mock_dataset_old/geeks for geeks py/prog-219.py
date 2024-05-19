test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
  
# printing original list
print("The original list is : " + str(test_list))
  
# performing sort, lambda function provides logic
res = sorted(test_list, key = lambda tup : sum([len(str(ele)) for ele in tup ]))
  
# printing result 
print("Sorted tuples : " + str(res))