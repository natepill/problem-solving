# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if root:
            # check left and right branches for path sum
            return self.calc_path(root.left, sum, root.val) or self.calc_path(root.right, sum, root.val)
        else:
            return False


    def calc_path(self, node, target, curr_sum=0):
        print(f"curr_sum = {curr_sum}")
        if curr_sum == target:
            return True

        if node:
            curr_sum += node.val
            if curr_sum == target:
                return True
            elif curr_sum < target:
                print(f"At {node.val} and curr_sum = {curr_sum}")
                return self.calc_path(node.left, target, curr_sum) or self.calc_path(node.right, target, curr_sum)
            else:
                return False


        else:

            return False if curr_sum != target else True


"""

    Popular Solution

"""

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    # 1:27
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
