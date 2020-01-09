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

    while curr_node is not None:
        # point curr_node towards prev_node
        curr_node.next = prev_node
        # set prev_node to curr_node
        prev_node = curr_node
        # curr_node set to next_node
        curr_node = next_node
        # next_node set to curr_node.next
        next_node = curr_node.next


    return prev_node

    # return prev_node
