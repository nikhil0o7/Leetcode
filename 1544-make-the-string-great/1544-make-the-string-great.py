class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) > 1:
                if stack[-1].lower() == stack[-2].lower():
                    if (stack[-1].isupper() and stack[-2].islower()) or (stack[-2].isupper() and stack[-1].islower()):
                        stack.pop()
                        stack.pop()
                
        return "".join(stack)
                