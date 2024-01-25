class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}
        for i in range(len(s)):
            c = s[i]
            if c in d:
                return c
            d[c] = i
        