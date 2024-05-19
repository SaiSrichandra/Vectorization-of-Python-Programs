# Python3 program to check missingNo

# Function to find the missing number
def getMissingNo(arr, n) :
	i = 0;
	
	while (i < n) :
		# as array is of 1 based indexing so the
		# correct position or index number of each
		# element is element-1 i.e. 1 will be at 0th
		# index similarly 2 correct index will 1 so
		# on...
		correctpos = arr[i] - 1;
		if (arr[i] < n and arr[i] != arr[correctpos]) :
			# if array element should be lesser than
			# size and array element should not be at
			# its correct position then only swap with
			# its correct position or index value
			arr[i],arr[correctpos] = arr[correctpos], arr[i]

		else :
			# if element is at its correct position
			# just increment i and check for remaining
			# array elements
			i += 1;
			
	# check for missing element by comparing elements with their index values
	for index in range(n) :
		if (arr[index] != index + 1) :
			return index + 1;
			
	return n;

# Driver code
if __name__ == "__main__" :
	arr = [ 1, 2, 3, 5 ];
	N = len(arr);
	print(getMissingNo(arr, N));


	# This Code is Contributed by AnkThon