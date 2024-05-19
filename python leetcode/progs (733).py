"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        return self.swapPairs_3

    def swapPairs_1(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
          prev.next = head.next
          head.next = head.next.next
          prev.next.next = head
          prev = head
          head = head.next
        return dummy.next

    def swapPairs_2(self, head):
        if head.next is None or head.next.next is None:
            return
        move = head.next.next
        head.next.next = move.next
        move.next = head.next.next
        head.next = move
        self.swapPairs_2(move.next)

    def swapPairs_3(self, head):
        if head is None or head.next is None:
            return head
        first = head
        second = head.next
        first.next = second.next
        second.next = first
        first.next = self.swapPairs_3(first.next)
        return second

    def swapPairs_3(self, head):
        # used one more variable
        dummy = ListNode(0)
        dummy.next = head
        current = head
        prev = dummy
        while current and current.next:
            next = current.next
            prev.next = next
            current.next = next.next
            next.next = current
            prev = current
            current = current.next

        return dummy.next
