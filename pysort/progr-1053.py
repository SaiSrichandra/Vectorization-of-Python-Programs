# Python program to sort an array
# of dates using Radix Sort
import sys

# Utilitiy function to obtain
# maximum date or month or year
def getMax(arr, n, q):
	maxi = sys.maxsize;
	for i in range(n):
		maxi = max(maxi, arr[i][q]);
	
	return maxi;

# A function to do counting sort of arr
# according to given q i.e.
# (0 for day, 1 for month, 2 for year)
def sortDatesUtil(arr, n, q):
	maxi = getMax(arr, n, q);
	p = 1;
	while (maxi > 0):
	
		# to extract last digit divide
		# by p then %10
		# Store count of occurrences in cnt
		cnt = [0 for i in range(10)];

		for i in range(n):
			cnt[(arr[i][q] // p) % 10]+=1;
		
		for i in range(1,10):
			cnt[i] += cnt[i - 1];
		
		ans = [[0 for i in range(3)] for j in range(n)];
		for i in range(n-1, -1,-1):
			lastDigit = (arr[i][q] // p) % 10;

			# Build the output array
			for j in range(3):
				ans[cnt[lastDigit] - 1][j] = arr[i][j];
			
			cnt[lastDigit] -= 1;
		
		# Copy the output array to arr,
		# so that arr now
		# contains sorted numbers
		# according to current digit
		for i in range(n):
			for j in range(3):
				arr[i][j] = ans[i][j];
			
		# update p to get
		# the next digit
		p *= 10;
		maxi = maxi//10;
	
# The main function that sorts
# array of dates
# using Radix Sort
def sortDates(dates, n):

	# First sort by day
	sortDatesUtil(dates, n, 0);

	# Then by month
	sortDatesUtil(dates, n, 1);
	
	# Finally by year
	sortDatesUtil(dates, n, 2);

# A utility function to print an array
def printArr(arr, n):
	for i in range(6):
		for j in range(3):
			print(arr[i][j], end=" ");
		
		print();
	
# Driver Code
if __name__ == '__main__':
	dates = [[ 20, 1, 2014 ],[ 25, 3, 2010 ],[ 3, 12, 2000 ],[ 18, 11, 2000 ],[ 19, 4, 2015 ],
			[ 9, 7, 2005 ]] ;
	n = len(dates);

	# Function Call
	sortDates(dates, n);
	print("\nSorted Dates");
	printArr(dates, n);

# This code is contributed by gauravrajput1