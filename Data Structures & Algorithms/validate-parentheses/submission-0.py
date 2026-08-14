class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ctp = {')': '(', '}': '{', ']' : '['}
        for i in s:
            if i in ctp:
                if not stack or stack[-1] != ctp[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return not stack