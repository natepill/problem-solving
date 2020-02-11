# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        traversal = []
        queue = [root]

        self.traverse(queue, traversal.append)

        return traversal

    def traverse(self, queue, visit):


        while queue:
            curr_lvl = []
            for _ in range(len(queue)):

                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                curr_lvl.append(node.val)

            visit(curr_lvl)







        
