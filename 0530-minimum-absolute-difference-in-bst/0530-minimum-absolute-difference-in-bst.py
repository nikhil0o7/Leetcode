# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            if node.left:
                dfs(node.left)
            ans.append(node.val)
            if node.right:
                dfs(node.right)
        
        ans = []
        dfs(root)
        res = float("inf")
        
        for i in range(1, len(ans)):
            res = min(res, ans[i] - ans[i - 1])
            
        return res
        