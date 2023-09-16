class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                d[arr[i]] +=1
            else:
                d[arr[i]] = 1
        a = []
        for i in d.values():
            a.append(i)
        return len(a) == len(set(a))


        