class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        i = len(nums)
        for x in range(i + 1):
            if x not in s:
                return x
        return 0
        
        