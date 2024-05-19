# Python3 code to demonstrate working of
# Unique Tuple Frequency [ Order Irrespective ]
# Using map() + sorted() + tuple() + set() + len()

# initializing lists
test_list = [(3, 4), (1, 2), (4, 3), (5, 6)]

# printing original list
print("The original list is : " + str(test_list))

# Using map() + sorted() + tuple() + set() + len()
# inner map used to perform sort and outer sort to
# convert again in tuple format
res = len(list(set(map(tuple, map(sorted, test_list)))))

# printing result
print("Unique tuples Frequency : " + str(res))