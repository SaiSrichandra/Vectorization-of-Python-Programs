# A Python program to check if any two intervals overlap

# An interval has start time and end time
class Interval:
	def __init__(self, start, end):
		self.start = start
		self.end = end

# Function to check if any two intervals overlap
def isIntersect(arr, n):

	# Sort intervals in increasing order of start time
	arr.sort(key=lambda x: x.start)

	# In the sorted array, if start time of an interval
	# is less than end of previous interval, then there
	# is an overlap
	for i in range(1, n):
		if (arr[i - 1].end > arr[i].start):
			return True

	# If we reach here, then no overlap
	return False

# Driver code
arr1 = [Interval(1, 3), Interval(7, 9), Interval(4, 6), Interval(10, 13)]
n1 = len(arr1)
if (isIntersect(arr1, n1)):
	print("Yes")
else:
	print("No")

arr2 = [Interval(6, 8), Interval(1, 3), Interval(2, 4), Interval(4, 7)]
n2 = len(arr2)

if (isIntersect(arr2, n2)):
	print("Yes")
else:
	print("No")

# This code is contributed by Saurabh Jaiswal