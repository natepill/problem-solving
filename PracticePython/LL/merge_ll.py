"""

    What I learned:

        This was a good review of Linked list problems over all. One thing that I learned is
        to wary of multi-conditional loops. Have to understand the state that I'm leaving the
        values in if they're changing in the loop and are a part of the conditional. I got slightly
        stuck when I wasn't understanding why a value was None, but the code above it ran fine. I hadn't
        understood that the value had become None after doing some iteration. 

        I would have been able to quicker identify the issue if I had a small test case that I
        ran EVERY line through.

    Biggest Takeaway: To debug create a Minimal Viable Test Case (MVTC) that can be quickly executed
    to identify the breaking point in the code.

"""





# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head_of_ll = None

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            head_of_ll = ListNode(l1.val)
            l1 = l1.next
        else:
            head_of_ll = ListNode(l2.val)
            l2 = l2.next

        new_node = head_of_ll
        # curr_l1 = l1
        # curr_l2 = l2

        while l1 is not None and l2 is not None:

            if l1.val <= l2.val:
                new_node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                new_node.next = ListNode(l2.val)
                l2 = l2.next

            new_node = new_node.next

        if l1 is not None:
            while l1 is not None:
                new_node.next = ListNode(l1.val)
                l1 = l1.next
                new_node = new_node.next

        if l2 is not None:
            while l2 is not None:
                new_node.next = ListNode(l2.val)
                l2 = l2.next
                new_node = new_node.next


        return head_of_ll





if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node4.next = node5
    node5.next = node6

    merged_list_head = mergeTwoLists(node1, node4)

    curr_node = merged_list_head
    while curr_node is not None:
        print(curr_node.val)
        curr_node = curr_node.next
