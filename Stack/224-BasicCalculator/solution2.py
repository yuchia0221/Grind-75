class Solution:
    def calculate(self, s: str) -> int:
        postfix_expression = convert_infix_to_postfix(s)
        return evaulate_postfix(postfix_expression)


def convert_infix_to_postfix(s: str) -> str:
    i = 0
    stack = []
    postfix_expression = ""
    operator_set = set("+-*/")
    operator_priority = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0, ")": 0}
    while i < len(s):
        token = s[i]
        if token == " ":
            i += 1
            continue
        elif token in operator_set:
            while stack and operator_priority[stack[-1]] >= operator_priority[token]:
                postfix_expression += stack.pop()

            stack.append(token)
        elif token == "(":
            stack.append(token)
            if s[i+1] == "-":
                postfix_expression += "0 "
        elif token == ")":
            while stack and stack[-1] != "(":
                postfix_expression += stack.pop()

            if stack:
                stack.pop()
        else:
            number = 0
            while i < len(s) and s[i].isdigit():
                number = number * 10 + int(s[i])
                i += 1
            postfix_expression += str(number) + " "
            i -= 1
        i += 1

    while stack:
        postfix_expression += stack.pop()

    return postfix_expression


def evaulate_postfix(s: str) -> int:
    i = 0
    stack = [0]
    operator_set = set("+-*/")
    while i < len(s):
        token = s[i]
        if token in operator_set:
            right_operand, left_operand = int(stack.pop()), int(stack.pop())
            if token == "+":
                result = left_operand + right_operand
            elif token == "-":
                result = left_operand - right_operand
            elif token == "*":
                result = left_operand * right_operand
            else:
                result = int(left_operand / right_operand)
            stack.append(result)
        elif token.isdigit():
            result = 0
            while i < len(s) and s[i] != " ":
                result = result * 10 + int(s[i])
                i += 1
            stack.append(result)
            i -= 1

        i += 1

    return stack[-1]
