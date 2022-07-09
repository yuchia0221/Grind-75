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
