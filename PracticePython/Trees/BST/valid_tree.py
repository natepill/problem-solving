# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        visited = []
        self.in_order_check(root, visited.append)
        return root is None or visited == sorted(visited)


    def in_order_check(self, node, visit):

        # print("here")
        if node:
            if node.left:
                self.in_order_check(node.left, visit)


            # order_stack.append(node.val)
            # print(order_stack)
            # This is replacing the "visit" operation in an in-order traversal
            # Checking to make sure values are in order
            # if order_stack:
            #     if order_stack[-1] < node.val:
            #         order_stack.append(node.val)
            #         print(order_stack)
            #     else:
            #         # print("asdasd")
            #         print(f"Out of order - Returning False: {order_stack}")
            #         return False
            # else:
            #     order_stack.append(node.val)
            #     print(f"First val {order_stack}")

            visit(node.val)

            if node.right:
                self.in_order_check(node.right, visit)


#         if not root:
#             return True

#         # is leaf
#         if root.left is None and root.right is None:
#             return True

#         if root.left is None:
#             return self.isValidBST(root.left)

#         if root.right is None:
#             return self.isValidBST(root.left)

#         if root.val < root.right.val and root.val > root.left.val:
#             return self.isValidBST(root.left) and self.isValidBST(root.right)
#         else:
#             return False
