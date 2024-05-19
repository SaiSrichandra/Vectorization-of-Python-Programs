# Python program to implement above approach

# picks up last element between start and end
import random

def findPivot(a, start, end):

	# Selecting the pivot element
	pivot = a[end]

	# Initially partition-index will be
	# at starting
	pIndex = start

	for i in range(start,end):

		# If an element is lesser than pivot, swap it.
		if (a[i] <= pivot):
			a[i],a[pIndex] = a[pIndex],a[i]

			# Incrementing pIndex for further
			# swapping.
			pIndex += 1
	

	# Lastly swapping or the
	# correct position of pivot
	a[end],a[pIndex] = a[pIndex],a[end]
	return pIndex


#THIS PART OF CODE IS CONTRIBUTED BY - rjrachit
#Picks up random pivot element between start and end
def findRandomPivot(arr, start, end):

	n = end - start + 1
	# Selecting the random pivot index
	pivotInd = (int((random.random()*1000000))%n)
	arr[end],arr[start+pivotInd] = arr[start+pivotInd],arr[end]
	pivot = arr[end]
	
	#initialising pivoting poto start index
	pivotInd = start
	for i in range(start,end):

		# If an element is lesser than pivot, swap it.
		if (arr[i] <= pivot):
			arr[i],arr[pivotInd] = arr[pivotInd],arr[i]

			# Incrementing pivotIndex for further
			# swapping.
			pivotInd += 1
		

	# Lastly swapping or the
	# correct position of pivot
	arr[pivotInd],arr[end] = arr[end],arr[pivotInd]
	return pivotInd


def SmallestLargest(a, low, high, k, n):
	if (low == high):
		return
	else:
		pivotIndex = findRandomPivot(a, low, high)

		if (k == pivotIndex):
			print(str(k)+ " smallest elements are :",end=" ")
			for i in range(pivotIndex):
				print(a[i],end = " ")

			print()

			print(str(k)+ " largest elements are :",end=" ")
			for i in range(n - pivotIndex,n):
				print(a[i],end=" ")

		elif (k < pivotIndex):
			SmallestLargest(a, low, pivotIndex - 1, k, n)

		elif (k > pivotIndex):
			SmallestLargest(a, pivotIndex + 1, high, k, n)
	
# Driver code
a = [ 11, 3, 2, 1, 15, 5, 4, 45, 88, 96, 50, 45 ]
n = len(a)

low = 0
high = n - 1

# assume k is 3
k = 3

# Function Call
SmallestLargest(a, low, high, k, n)

# This code is contributed by shinjanpatra