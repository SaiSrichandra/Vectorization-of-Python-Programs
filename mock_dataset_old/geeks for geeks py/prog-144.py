test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]
 
# printing both lists
print ("The original list 1 : " + str(test_list1))
print ("The original list 2 : " + str(test_list2))
 
# using map() + set() + ^
# Uncommon elements in Lists of List
res_set = set(map(tuple, test_list1)) ^ set(map(tuple, test_list2))
res_list = list(map(list, res_set))
 
# printing the uncommon
print ("The uncommon of two lists is : " + str(res_list))