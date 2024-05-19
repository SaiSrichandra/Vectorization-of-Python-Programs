# Python3 code to demonstrate working of
# Consecutive Kth column Difference in Tuple List
# Using zip() + list comprehension

# initializing list
test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 1

# zip used to pair each tuple with subsequent tuple
res = [abs(x[K] - y[K]) for x, y in zip(test_list, test_list[1:])]
	
# printing result
print("Resultant tuple list : " + str(res))