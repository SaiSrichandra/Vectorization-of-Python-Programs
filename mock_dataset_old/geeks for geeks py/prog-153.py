def prod(val) :
    res = 1
    for ele in val:
        res *= ele
    return res 
 
# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))
 
# using list comprehension
# Duplication Removal List Product
res = []
[res.append(x) for x in test_list if x not in res]
res = prod(res)
 
# printing list after removal
print ("Duplication removal list product : " + str(res))