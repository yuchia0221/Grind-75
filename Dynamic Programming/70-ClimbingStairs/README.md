# Climbing Stairs

Problem can be found in [here](https://leetcode.com/problems/climbing-stairs)!

### [Solution](/Dynamic%20Programming/70-ClimbingStairs/solution.py): Dynamic Programming

```python
def memoization(func):
    memo = {}

    def helper(self, x):
        if x not in memo:
            memo[x] = func(self, x)
        return memo[x]
    return helper


class Solution:
    @memoization
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)
```

Explanation: Basically, it is a Fibonacci sequence. I just use memoization to optimize time complexity.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is value of $n$ steps to climb.
