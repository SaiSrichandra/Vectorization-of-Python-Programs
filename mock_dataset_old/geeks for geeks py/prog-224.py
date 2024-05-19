from collections import Counter
 
# initializing list
test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# one-liner to solve problem
# assign Frequency as last element of tuple
res = [(*key, val) for key, val in Counter(test_list).items()]
 
# printing results
print("Frequency Tuple list : " + str(res))