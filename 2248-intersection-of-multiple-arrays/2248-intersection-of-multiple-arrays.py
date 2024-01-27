from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(int)
        n = len(nums)
        ans = []
        for arr in nums:
            for i in arr:
                d[i] +=1
        for key in d:
            if d[key] == n:
                ans.append(key)
        return sorted(ans)