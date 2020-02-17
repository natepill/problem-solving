

def invert(root):

    if not root:
        return root


    left  = invert(root.left)
    right = invert(root.right)


    # swap

    root.left = right
    root.right = left
    
