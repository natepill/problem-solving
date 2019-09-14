# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

#  Old code iterative version

#         head_node = head.next
#         curr_node = head
#         next_node = curr_node.next
#         post_node = next_node.next


#         while curr_node.next is not None:
#             next_node.next = curr_node
#             curr_node = post_node
#             next_node = curr_node.next

    # My recursive refactor

        if not head or not head.next:
            return head

        curr_node = head
        next_node = head.next
        # next_node.next seems to be the third node, similar to post_node
        next_node.next = self.swapPairs(next_node.next)
        next_node.next = head


# Copied Soltution

        temp=head
        temp2=head.next
        temp.next=self.swapPairs(temp2.next)
        temp2.next=temp
        return temp2
