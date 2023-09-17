class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumA = 0
        r = sum(nums)
        for i in range(len(nums)):
            r -= nums[i]
            if sumA == r:
                return i
            sumA += nums[i]
        return -1