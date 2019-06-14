class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    l1_curr = l1
    l2_curr = l2

    answer_node_curr = None
    answer_node_head = None

    carry_over = False


    while l1_curr is not None and l2_curr is not None:
        base_sum = l1_curr.val + l2_curr.val

        # Carry over is always going to add one if indicated by carry over flag
        node_sum = base_sum if carry_over == False else base_sum + 1

        # Sum is larger than 9 implies carry over
        if node_sum > 9:

            # First iteration to set appropriate values
            if answer_node_curr is None:
                # mod 10 gets us the remainder of what doesn't need to be carried over
                answer_node_curr = ListNode(node_sum%10)
                # We need to track the head node of our answer list because there is no LL class
                answer_node_head = answer_node_curr

            else:

                answer_node_curr.next = ListNode(base_sum%10)

            # Carry over to be done next iteration
            carry_over = True

        else:
            if answer_node_curr is None:
                answer_node_curr = ListNode(base_sum)
                answer_node_head = answer_node_curr
            else:
                answer_node_curr.next = ListNode(base_sum)

            # No carry over to be done next iteration
            carry_over = False

        # Traverse both LL

        # No more addition
        if l1_curr.next is None and l2_curr.next is None:
            break

        # both lists can be traversed
        elif l1_curr.next is not None and l2_curr.next is not None:
            l1_curr = l1_curr.next
            l2_curr = l2_curr.next

        # list 1 is longer than list 2
        elif l1_curr.next is not None and l2_curr.next is None:
            l1_curr = l1_curr.next
            l2_curr.next = ListNode(0)
            l2_curr = l2_curr.next

        # list 1 is shorter than list 2
        elif l1_curr.next is None and l2_curr.next is not None:
            l1_curr.next = ListNode(0)
            l1_curr = l1_curr.next
            l2_curr = l2_curr.next


def print_ll(head_node):

    node = head_node
    value = ''
    while node is not None:
        value += str(node.val)
        node = node.next

    return value


if __name__ == "__main__":

    l1 = ListNode(2)
    l1a = ListNode(3)
    l1.next = l1a
    l1a.next = ListNode(6)

    print(print_ll(l1))

    # l2 = ListNode(5)
    # l2a = ListNode(3)
    # l2.next = l2a
    # l2a.next = ListNode(7)
    #
    #
    # addTwoNumbers(l1, l2)
