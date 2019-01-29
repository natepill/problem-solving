from linked_list import LinkedList

class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):

    def __init__(self, data):
        self.root = Node(data)

    def add(self, data, root):
        new_node = Node(data)
        curr_node = self.root

        if root.data < new_node.data:
            curr_node = self.left






        else:
            curr_node = self.right
