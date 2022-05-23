from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            else:
                right_operand, left_operand = stack.pop(), stack.pop()
                if token == "+":
                    result = (left_operand + right_operand)
                elif token == "-":
                    result = (left_operand - right_operand)
                elif token == "*":
                    result = (left_operand * right_operand)
                else:
                    result = int(left_operand / right_operand)
                stack.append(result)

        return stack[-1]
