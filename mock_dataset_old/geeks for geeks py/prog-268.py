# Python3 code to demonstrate working of
# Convert Matrix to Custom Tuple Matrix
# Using list comprehension + zip()

# initializing lists
test_list = [[4, 5, 6], [6, 7, 3], [1, 3, 4]]

# printing original list
print("The original list is : " + str(test_list))

# initializing List elements
add_list = ['Gfg', 'is', 'best']

# Convert Matrix to Custom Tuple Matrix
# Using list comprehension + zip()
res = [(ele1, ele2) for ele1, sub in zip(add_list, test_list) for ele2 in sub]

# printing result
print("Matrix after conversion : " + str(res))