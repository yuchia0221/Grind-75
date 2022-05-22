# Implement Queue using Stacks

Problem can be found in [here](https://leetcode.com/problems/implement-queue-using-stacks/)!

### [Solution](/Stack/232-ImplementQueueusingStacks/solution.py)

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not (self.in_stack or self.out_stack)
```

Amortized Time Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
