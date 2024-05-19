test_list = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initializing K
K = 6
  
# filter() + lambda for filter operation
res = list(filter(lambda sub: all(ele % K == 0 for ele in sub), test_list))
  
# printing result
print("K Multiple elements tuples : " + str(res))