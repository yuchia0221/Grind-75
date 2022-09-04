# Min Stack

Problem can be found in [here](https://leetcode.com/problems/min-stack)!

### [Solution](/Stack/155-MinStack/solution.py)

```python
class MinStack:
    def __init__(self):
        self.stack = [float("inf")]

    def push(self, val: int) -> None:
        min_value = self.stack[-1]
        self.stack.append(val)
        self.stack.append(min(min_value, val))

    def pop(self) -> None:
        self.stack.pop()
        self.stack.pop()

    def top(self) -> int:
        min_value = self.stack.pop()
        current_value = self.stack.pop()
        self.stack.append(current_value)
        self.stack.append(min_value)
        return current_value

    def getMin(self) -> int:
        return self.stack[-1]
```

Time Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
