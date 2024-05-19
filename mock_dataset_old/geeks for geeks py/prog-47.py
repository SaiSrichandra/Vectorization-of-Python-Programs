test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing K
K = 'e'
 
# "-" sign used to reverse sort
res = sorted(test_list, key = lambda ele: -ele.count(K))
 
# printing results
print("Sorted String : " + str(res))