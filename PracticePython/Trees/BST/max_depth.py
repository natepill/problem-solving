# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        left_height = 0
        right_height = 0

        if not root.left and not root.right:
            return 1

        if root.left:
            left_height = self.maxDepth(root.left)


        if root.right:
            right_height = self.maxDepth(root.right)


        node_height = left_height if left_height > right_height else right_height

        return node_height + 1



"""
    More elegant recursive solution
"""


class Solution:
    def maxDepth(self, root: TreeNode) -> int:


        if root is None:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)
