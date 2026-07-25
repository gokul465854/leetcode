# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        # Dummy nodes
        small_dummy = ListNode(0)
        large_dummy = ListNode(0)

        # Pointers
        small = small_dummy
        large = large_dummy

        current = head

        while current:

            if current.val < x:
                small.next = current
                small = small.next
            else:
                large.next = current
                large = large.next

            current = current.next

        # End the larger list
        large.next = None

        # Connect both lists
        small.next = large_dummy.next

        return small_dummy.next