# Python3 code to demonstrate working of
# Tuple List intersection [ Order irrespective ]
# Using list comprehension + map() + frozenset() + & operator

# initializing lists
test_list1 = [(3, 4), (5, 6), (9, 10), (4, 5)]
test_list2 = [(5, 4), (3, 4), (6, 5), (9, 11)]

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Using list comprehension + map() + frozenset() + & operator
# frozenset used as map() requires hashable container, which
# set is not, result in frozenset format
res = set(map(frozenset, test_list1)) & set(map(frozenset, test_list2))

# printing result
print("List after intersection : " + str(res))