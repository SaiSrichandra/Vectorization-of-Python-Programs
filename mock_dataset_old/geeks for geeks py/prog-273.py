# Python3 code to demonstrate working of
# Extract K digit Elements Tuples
# Using all() + filter() + lambda

# initializing list
test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# filter() and lambda used for task of filtering
res = list(filter(lambda sub: all(len(str(ele)) == K for ele in sub), test_list))

# printing result
print("The Extracted tuples : " + str(res))