# Python3 code to demonstrate working of
# Convert Binary tuple to Integer
# Using bit shift and | operator

# initializing tuple
test_tup = (1, 1, 0, 1, 0, 0, 1)

# printing original tuple
print("The original tuple is : " + str(test_tup))


res = 0
for ele in test_tup:
	
	# left bit shift and or operator
	# for intermediate addition
	res = (res << 1) | ele

# printing result
print("Decimal number is : " + str(res))