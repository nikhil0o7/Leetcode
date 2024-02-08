# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if root.right is None  and root.left is None:
            return 1
        elif root.right is None:
            return 1 + left
        elif root.left is None:
            return 1+ right
        return min(left,right) + 1

        