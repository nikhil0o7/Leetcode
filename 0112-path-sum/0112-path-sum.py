# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def rootSum(node, curr):
            if not node:
                return None
            
            if node.left == None and node.right == None:
                return curr + node.val == targetSum
            curr += node.val
            left = rootSum(node.left, curr)
            right = rootSum(node.right , curr)
            return left or right
        return rootSum(root, 0)
        