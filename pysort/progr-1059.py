# Python3 program to find a list in second list
class Node:
	def __init__(self, value = 0):
		
		self.value = value
		self.next = None

# Returns true if first list is
# present in second list
def findList(first, second):
	
	# If both linked lists are empty/None,
	# return True
	if not first and not second:
		return True

	# If ONLY one of them is empty,
	# return False
	if not first or not second:
		return False

	ptr1 = first
	ptr2 = second

	# Traverse the second LL by
	# picking nodes one by one
	while ptr2:

		# Initialize 'ptr2' with current
		# node of 'second'
		ptr2 = second

		# Start matching first LL
		# with second LL
		while ptr1:

			# If second LL become empty and
			# first not, return False,
			# since first LL has not been
			# traversed completely
			if not ptr2:
				return False

			# If value of both nodes from both
			# LLs are equal, increment pointers
			# for both LLs so that next value
			# can be matched
			elif ptr1.value == ptr2.value:
				ptr1 = ptr1.next
				ptr2 = ptr2.next

			# If a single mismatch is found
			# OR ptr1 is None/empty,break out
			# of the while loop and do some checks
			else:
				break

		# check 1 :
		# If 'ptr1' is None/empty,that means
		# the 'first LL' has been completely
		# traversed and matched so return True
		if not ptr1:
			return True

		# If check 1 fails, that means, some
		# items for 'first' LL are still yet
		# to be matched, so start again by
		# bringing back the 'ptr1' to point
		# to 1st node of 'first' LL
		ptr1 = first
		
		# And increment second node element to next
		second = second.next
		
	return False

# Driver Code

# Let us create two linked lists to
# test the above functions.
# Created lists would be be
# node_a: 1->2->3->4
# node_b: 1->2->1->2->3->4
node_a = Node(1)
node_a.next = Node(2)
node_a.next.next = Node(3)
node_a.next.next.next = Node(4)

node_b = Node(1)
node_b.next = Node(2)
node_b.next.next = Node(1)
node_b.next.next.next = Node(2)
node_b.next.next.next.next = Node(3)
node_b.next.next.next.next.next = Node(4)

if findList(node_a, node_b):
	print("LIST FOUND")
else:
	print("LIST NOT FOUND")

# This code is contributed by GauriShankarBadola