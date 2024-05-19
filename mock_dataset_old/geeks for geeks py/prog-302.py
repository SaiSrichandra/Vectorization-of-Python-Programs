# Python3 code to demonstrate working of
# Skew Nested Tuple Summation
# Using recursion

# helper function to perform task
def tup_sum(test_tup):
	
	# return on None
	if not test_tup:
		return 0
	else:
		return test_tup[0] + tup_sum(test_tup[1])

# initializing tuple
test_tup = (5, (6, (1, (9, (10, None)))))

# printing original tuple
print("The original tuple is : " + str(test_tup))

# calling fnc.
res = tup_sum(test_tup)

# printing result
print("Summation of 1st positions : " + str(res))