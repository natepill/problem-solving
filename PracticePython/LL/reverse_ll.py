"""

    Be quicker to MVTC to debug.

    Review the recursive solution

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # init backwards to None

        # keep reversing until end of LL
            # store next pointer
            # point curr_node backwards
            # backwards becomes curr_node
            # curr_node becomes next_node

        # node pointers
        prev_node = None
        curr_node = head
        # next_node = head.next

        # keep reversing until end of LL
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node
