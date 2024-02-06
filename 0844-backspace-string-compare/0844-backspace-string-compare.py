class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack, stck = [], []
        for i in s:
            if i == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        for i in t:
            if i == "#":
                if stck:
                    stck.pop()
            else:
                stck.append(i)
        return stack == stck
            
            
            
        