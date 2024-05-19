# Python program to sort a list of
# tuples using sorted()
	
# Function to sort the list
def Sort_Tuple(tup):
	
	# reverse = None (Sorts in Ascending order)
	# key is set to sort using first element of
	# sublist lambda has been used
	return(sorted(tup, key = lambda x: x[0]))
	
# Driver Code
tup = [("Amana", 28), ("Zenat", 30), ("Abhishek", 29),
		("Nikhil", 21), ("B", "C")]
	
# printing the sorted list of tuples
print(Sort_Tuple(tup))