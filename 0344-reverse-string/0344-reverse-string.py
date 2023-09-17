class Solution:
    def reverseString(self, s: List[str]) -> None:
        a,b = 0, len(s)-1
        i = 0
        while a < b:
            s[a],s[b] = s[b],s[a]
            a+=1
            b -=1
            
        