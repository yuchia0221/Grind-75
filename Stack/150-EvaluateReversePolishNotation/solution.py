from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in set("+-*/"):
                right_operand, left_operand = int(stack.pop()), int(stack.pop())
                if token == "+":
                    result = (left_operand + right_operand)
                elif token == "-":
                    result = (left_operand - right_operand)
                elif token == "*":
                    result = (left_operand * right_operand)
                else:
                    result = int(left_operand / right_operand)
                stack.append(result)
            else:
                stack.append(token)

        return stack[-1]

