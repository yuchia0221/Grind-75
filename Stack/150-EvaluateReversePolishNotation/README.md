# Evaluate Reverse Polish Notation

Problem can be found in [here](https://leetcode.com/problems/evaluate-reverse-polish-notation)!

### [Solution](/Stack/150-EvaluateReversePolishNotation/solution.py)

```python
def evalRPN(tokens: List[str]) -> int:
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
