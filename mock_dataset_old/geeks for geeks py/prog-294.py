# Python3 code to demonstrate working of
# Closest Pair to Kth index element in Tuple
# Using min() + lambda

# initializing list
test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]

# printing original list
print("The original list is : " + str(test_list))

# initializing tuple
tup = (17, 23)

# initializing K
K = 1

# Closest Pair to Kth index element in Tuple
# Using min() + lambda
res = min(range(len(test_list)), key = lambda sub: abs(test_list[sub][K - 1] - tup[K - 1]))

# printing result
print("The nearest tuple to Kth index element is : " + str(test_list[res]))