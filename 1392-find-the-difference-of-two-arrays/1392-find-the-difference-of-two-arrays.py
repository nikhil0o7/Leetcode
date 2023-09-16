class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ks = set(nums1)
        ka = set(nums2)
        out = [[],[]]
        for i in ks:
            if i not in ka:
                out[0].append(i)
        for i in ka:
            if i not in ks:
                out[1].append(i)
        return out
        




        