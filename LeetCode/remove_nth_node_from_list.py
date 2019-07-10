"""

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):

    # init index counter
    # Traverse LL
        # Store node values as values to index key value pairs: index:value

    # init target_index = index_counter (which is now at end of LL) - n
    # reset index counter to 0

    # Traverse LL again
        # Stop when index_counter = target_index
        # remove node at index and connect prev node to next node

    if head.next is None:
        return None


    index = 0
    curr_node = head
    prev_node = head
    node_indexes = []

    while curr_node is not None:
        node_indexes.append(index)
        curr_node = curr_node.next
        index += 1

    index = 0
    target_index = node_indexes[n*-1]
    curr_node = head
    print("TARGET INDEX:", target_index)
    while curr_node is not None:
        print("target_index:", str(target_index) + " current_index:", str(index))
        # print("index:", index)
        if index == target_index:

            if prev_node is curr_node:
                print("asdasdas")
                head = curr_node.next
                print("VL:",head.val)
                break

            prev_node.next = curr_node.next
            break

        prev_node = curr_node
        curr_node = curr_node.next

        index += 1


    return head




if __name__ == "__main__":
    # nums = [1,2]


    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2


    # node1 = ListNode("alpha")
    # node2 = ListNode("beta")
    # node1.next = node2
    # node3 = ListNode("gamma")
    # node2.next = node3
    removeNthFromEnd(node1, 2)

    curr_node = node1
    while curr_node is not None:
        print(curr_node.val)
        curr_node = curr_node.next
