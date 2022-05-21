class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in set("([{"):
                stack.append(char)
            else:
                if not stack or bracket[stack[-1]] != char:
                    return False
                else:
                    stack.pop()

        return not stack
