class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i , j = 0, len(nums) - 1
        result = [0] * len(nums)
        for x in range(len(nums)-1, -1 , -1):
            if abs(nums[i]) > abs(nums[j]):
                sq = nums[i]
                i +=1
            else:
                sq = nums[j]
                j -=1
            result[x] = sq * sq
        return result