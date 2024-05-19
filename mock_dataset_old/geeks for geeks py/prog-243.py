test_list1 = [(1, 7), (6, 7), (9, 100), (4, 21)]
test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]
  
# printing original lists
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))
  
# zip() is used for pairing 
res = [(a[1], b[1]) for a, b in zip(test_list1, test_list2) if a[0] == b[0]]
  
# printing result 
print("The mapped tuples : " + str(res))