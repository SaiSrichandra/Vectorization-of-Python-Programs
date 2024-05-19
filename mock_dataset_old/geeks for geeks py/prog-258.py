# Python3 code to demonstrate working of
# Custom sorting in list of tuples
# Using sorted() + lambda() + sum()

# Initializing list
test_list = [(7, (8, 4)), (5, (6, 1)), (7, (5, 3)), (10, (5, 4)), (10, (1, 3))]

# printing original list
print("The original list is : " + str(test_list))

# Custom sorting in list of tuples
# Using sorted() + lambda() + sum()
res = sorted(test_list, key = lambda sub: (-sub[0], sum(sub[1])))

# printing result
print("The tuple after custom sorting is : " + str(res))