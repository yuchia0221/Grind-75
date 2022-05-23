# Valid Parentheses

Problem can be found in [here](https://leetcode.com/problems/valid-parentheses)!

### [Solution](/Stack/20-ValidParentheses/solution.py)

```python
def isValid(s: str) -> bool:
    stack = []
    bracket = {"(": ")", "[": "]", "{": "}"}
    for char in s:
        # Case 1: Left Bracket, just simply push into stack
        if char in set("([{"):
            stack.append(char)
        # Case 2: Right Bracket, may cause invalid parentheses
        else:
            if not stack or bracket[stack[-1]] != char:
                return False
            else:
                stack.pop()

    return not stack
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
