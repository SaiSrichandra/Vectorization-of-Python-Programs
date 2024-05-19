# Python3 code to demonstrate working of
# Sort by Frequency of second element in Tuple List
# Using Counter() + lambda + sorted()
from collections import Counter

# initializing list
test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]

# printing original list
print("The original list is : " + str(test_list))

# constructing mapping using Counter
freq_map = Counter(val for key, val in test_list)

# performing sort of result
res = sorted(test_list, key = lambda ele: freq_map[ele[1]], reverse = True)

# printing results
print("Sorted List of tuples : " + str(res))