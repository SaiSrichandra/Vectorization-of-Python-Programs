# Python 3 program for the above approach

def maxInBitonic(arr, l, r) :

	while (l <= r) :

		m = int(l + (r - l) / 2) # m = (l + r) / 2

		#Base Cases Starts*****/
		
		if(l==r):
			return arr[l];
	
		# If there are two elements and first is greater
		# then the first element is maximum */
		if ((r == l + 1) and arr[l] >= arr[r]):
			return arr[l]

		# If there are two elements and second is greater
		# then the second element is maximum */

		if ((r == l + 1) and arr[l] < arr[r]):
			return arr[r]

		# If we reach a point where arr[mid] is greater
		# than both of its adjacent elements arr[mid-1] and
		# arr[mid+1], then arr[mid] is the maximum
		# element*/
		if (arr[m] > arr[m + 1] and arr[m] > arr[m - 1]):
			return arr[m]

		#***Base Case ends *****/

		# move to left with l and r=m-1
		if (arr[m] > arr[m + 1] and arr[m] < arr[m - 1]) :
			r = m - 1

		else :
			l = m + 1 # move to right with l=m+1 and r
	
	# if we reach here, then element was
	# not present
	return -1

# Driver function
arr = [ 1, 3, 50, 10, 9, 7, 6 ]
n = len(arr)
print("The maximum element is ", maxInBitonic(arr, 0, n - 1))

# This code is contributed by splevel62.