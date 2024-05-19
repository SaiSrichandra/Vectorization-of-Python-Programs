# Python program to sort a list of
# tuples using sort()
	
# Function to sort the list
def SortTuple(tup):
	
	# reverse = None (Sorts in Ascending order)
	# key is set to sort using first element of
	# sublist lambda has been used
	tup.sort(key = lambda x: x[0])
	return tup
	
# Driver's code

tup = [("Amana", 28), ("Zenat", 30), ("Abhishek", 29),
		("Nikhil", 21), ("B", "C")]
		
print(SortTuple(tup))