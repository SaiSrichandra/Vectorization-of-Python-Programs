test_list = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initializing K 
K = 6
  
# Remove Consecutive K element records
# Using zip() + list comprehension
res = [idx for idx in test_list if (K, K) not in zip(idx, idx[1:])]
  
# printing result 
print("The records after removal : " + str(res))