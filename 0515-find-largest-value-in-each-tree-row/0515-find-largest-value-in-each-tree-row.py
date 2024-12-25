# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q= deque([root])
        ans = []

        while q:
            curr_len = len(q)
            curr_max = float("-inf")

            for _ in range(curr_len):
                node = q.popleft()
                curr_max = max(curr_max, node.val)

                if node.right:
                    q.append(node.right)

                if node.left:
                    q.append(node.left)

            ans.append(curr_max)

        return ans
