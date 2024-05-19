# Python code for the above approach
class GFG:
	def main(args):
		# Input:
		arr = [4, 3, 6, 2, 1, 1]
		n = len(arr)
		
		# Declaring output variables
		# Note : arr[i]-1 is used instead of arr[i] as we want to use all 64 bits
		bitOr = (1 << (arr[0] - 1))
		repeating = 0
		missing = 0
		
		# Performing XOR as well as Checking repeating number
		for i in range(1, n):
		
			# If OR operation with 1 gives same output
			# that means, we already have 1 at that position
			if ((bitOr | (1 << (arr[i] - 1))) == bitOr):
				repeating = arr[i]
				continue
			bitOr = (bitOr | (1 << (arr[i] - 1)))
			
		# Checking missing number
		for i in range(1, n):
		
			# property: OR with 0 yield 1 hence value of bitOr changes
			if ((bitOr | (1 << i)) != bitOr):
				missing = i + 1
				break

		print("Repeating : " + str(repeating) + "\nMissing : " + str(missing))

if __name__ == "__main__":
	GFG.main([])

# This code is contributed by Mukul Jatav (mukulsomukesh)