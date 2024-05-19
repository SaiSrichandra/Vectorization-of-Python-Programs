# Python3 code to demonstrate working of
# Sort Tuples by Maximum element
# Using sort() + lambda + reverse

# initializing list
test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]

# printing original list
print("The original list is : " + str(test_list))

# lambda function getting maximum elements
# reverse for sorting by max - first element's tuples
test_list.sort(key = lambda sub : max(sub), reverse = True)

# printing result
print("Sorted Tuples : " + str(test_list))