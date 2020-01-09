# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # prev_node (None)
        # curr_node
        # next_node


        # save next_node as temp
        # point curr_node towards prev_node
        # set prev_node to curr_node
        # curr_node set to next_node
        # next_node set to curr_node.next
        # next_node becomes curr_node

        # return prev_node
