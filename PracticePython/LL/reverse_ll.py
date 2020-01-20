"""

    Be quicker to MVTC to debug.

    Review the recursive solution

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:

    # prev_node (None)
    # curr_node
    # next_node
    prev_node = None
    curr_node = head
    next_node = head.next

    while next_node is not None:
        # point curr_node towards prev_node
        curr_node.next = prev_node
        # set prev_node to curr_node
        prev_node = curr_node
        # curr_node set to next_node
        curr_node = next_node
        # next_node set to curr_node.next
        next_node = curr_node.next


    curr_node.next = prev_node

    return curr_node








class Solution:

    def helper(self, prev, cur):

        if cur:

            # locate next hopping node
            next_hop = cur.next

            # reverse direction
            cur.next = prev

            return self.helper( cur, next_hop)

        else:

            # new head of reverse linked list
            return prev


    def reverseList(self, head: ListNode) -> ListNode:

        return self.helper( None, head)
