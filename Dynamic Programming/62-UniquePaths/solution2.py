class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                memo[j] = memo[j - 1] + memo[j]
        return memo[-1] if m and n else 0
