# Unique Paths

Problem can be found in [here](https://leetcode.com/problems/unique-paths)!

### [Solution 1](/Dynamic%20Programming/62-UniquePaths/solution1.py): Math

```python
def uniquePaths(m: int, n: int) -> int:
    return comb(m+n-2, n-1)
```

Explanation: There are m+n-2 steps to move from top-left to bottom-right. In m+n-2 steps, there are m-1 steps we have to move down and n-1 steps we have to move right. Simply put, we need to calculate how many ways we could choose m-1 down moves from m+n-2 moves, or n-1 right moves from m+n-2 moves. Therefore, the solution is ![C_{n-1}^{m+n-2}](https://latex.codecogs.com/svg.image?C_{n-1}^{m+n-2}).

Time Complexity: ![O(m+n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m+n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where m is the number of rows and n is the number of columns.

### [Solution 2](/Dynamic%20Programming/62-UniquePaths/solution2.py): Dynamic Programming

```python
def uniquePaths(m: int, n: int) -> int:
    memo = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            memo[j] = memo[j - 1] + memo[j]
    return memo[-1] if m and n else 0
```

Time Complexity: ![O(m+n)](<https://latex.codecogs.com/svg.image?\inline&space;O(m+n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where m is the number of rows and n is the number of columns.
