# Function to get the missing number
def getMissingNo(a, n):
	i, total = 0, 1

	for i in range(2, n + 2):
		total += i
		total -= a[i - 2]
	return total


# Driver Code
if __name__ == '__main__':
	arr = [1, 2, 3, 5]
	N = len(arr)

	# Function call
	print(getMissingNo(arr, N))

# This code is contributed by Mohit kumar