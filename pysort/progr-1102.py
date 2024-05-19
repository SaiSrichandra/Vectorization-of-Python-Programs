# Python program to find a pair with the given difference

# The function assumes that the array is sorted
def findPair(arr, size, n):

	mpp = {}

	for i in range(size):
		if arr[i] in mpp.keys():
			mpp[arr[i]] += 1
			if(n == 0 and mpp[arr[i]] > 1):
				return true;
		else:
			mpp[arr[i]] = 1
	
	if(n == 0):
		return false;

	for i in range(size):
		if n + arr[i] in mpp.keys():
			print("Pair Found: (" + str(arr[i]) + ", " + str(n + arr[i]) + ")")
			return True
	
	print("No Pair found")
	return False

# Driver program to test above function
arr = [ 1, 8, 30, 40, 100 ]
size = len(arr)
n = -60
findPair(arr, size, n)

# This code is contributed by shinjanpatra