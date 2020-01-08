# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    head_of_ll = ListNode(l1.val) if l1.val < l2.val else ListNode(l2.val)
    new_node = head_of_ll
    # curr_l1 = l1
    # curr_l2 = l2

    while l1 != None or l2 is not None:

        if l1.val <= l2.val:
            new_node.next = ListNode(l1.val)
            l1 = l1.next
        else:
            new_node.next = ListNode(l2.val)
            l2 = l2.next


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
