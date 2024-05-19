test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# all() to check each element
res = list(filter(lambda sub: all(ele >= 0 for ele in sub), test_list))
 
# printing result
print("Positive elements Tuples : " + str(res))