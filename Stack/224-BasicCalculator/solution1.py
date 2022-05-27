class Solution:
    def calculate(self, s: str) -> int:
        def helper(index: int):
            def evaluation(operator: str, number: int) -> None:
                nonlocal stack
                if operator == "+":
                    stack.append(number)
                elif operator == "-":
                    stack.append(-number)
                elif operator == "*":
                    stack.append(stack.pop() * number)
                elif operator == "/":
                    stack.append(int(stack.pop() / number))

            operator_set = set("+-*/")
            number, operator, stack = 0, "+", []
            while index < len(s):
                token = s[index]
                if token.isdigit():
                    number = int(token)
                    while index < len(s)-1 and s[index+1].isdigit():
                        number = 10*number + int(s[index+1])
                        index += 1

                elif token in operator_set:
                    evaluation(operator, number)
                    number, operator = 0, token
                elif token == "(":
                    number, index = helper(index+1)
                elif token == ")":
                    evaluation(operator, number)
                    return sum(stack), index

                index += 1

            evaluation(operator, number)
            return sum(stack)

        return helper(0)
