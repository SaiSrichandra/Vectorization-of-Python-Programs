# Python code to implement the approach

# Function to count occurrences
def countOccurrences(arr, x) :

	count = 0
	n = len(arr)
	for i in range(n) :
		if (arr[i] == x):
			count += 1
			
	return count
	
# Driver Code
if __name__ == "__main__":
		
	arr = [ 1, 2, 2, 2, 2, 3, 4, 7, 8, 8 ]
	x = 2

	# displaying the frequency of x in ArrayList
	print(x , "occurs"
						, countOccurrences(arr, x)
						, "times")
	
	# This code is contributed by sanjoy_62.