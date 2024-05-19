# Python program to find the missing
# and repeating element
def swap(arr, a, b):
	temp = arr[a]
	arr[a] = arr[b]
	arr[b] = temp

def getTwoElements(arr, n):
	repeating = 0
	missing = 0

	i = 0

	# Traverse on the array
	while (i < n):

		# If the element is on its correct position
		if (arr[i] == arr[arr[i] - 1]):
			i += 1
		else:
		# If it is not at its correct position
			# then palce it to its correct position
			swap(arr, i, arr[i] - 1)

	# Find repeating and missing
	for i in range(n):

		# If any element is not in its correct position
		if (arr[i] != i + 1):
			repeating = arr[i]
			missing = i + 1
			break

	# Print answer
	print("Repeating:", repeating)
	print("Missing:", missing)

# Driver code
arr = [2, 3, 1, 5, 1]
n = len(arr)
getTwoElements(arr, n)

# This code is contributed by Tapesh (tapeshdua420)