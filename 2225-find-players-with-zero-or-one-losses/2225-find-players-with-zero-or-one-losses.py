class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        seen =set()
        d = {}
        for w,l in matches:
            seen.add(w)
            seen.add(l)
            d[l] = d.get(l,0) +1
        w, l = [], []
        for i in seen:
            c = d.get(i,0)
            if c == 0:
                w.append(i)
            elif c ==1:
                l.append(i)
        return [sorted(w),sorted(l)]
            
            
            
        