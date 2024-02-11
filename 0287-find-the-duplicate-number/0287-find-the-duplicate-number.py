class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t = {}
        k = t.keys()
        for i in nums:
            if i not in k:
                t[i] =1 
            else:
                return i
        return None