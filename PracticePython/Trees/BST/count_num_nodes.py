

def count_nodes(root):
    return  count_nodes(node.left) + count_nodes(node.right) + 1 if node else 0
