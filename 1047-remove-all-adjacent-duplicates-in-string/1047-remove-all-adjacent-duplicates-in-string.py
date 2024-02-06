class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            print(c)
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        print(s)
        return "".join(stack)