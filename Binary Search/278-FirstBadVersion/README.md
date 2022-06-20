# First Bad Version

Problem can be found in [here](https://leetcode.com/problems/first-bad-version)!

```python
# The isBadVersion API is defined as followed
def isBadVersion(version: int) -> bool:
    ...
```

### [Solution](/Binary%20Search/278-FirstBadVersion/solution.py)

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left+right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
```

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
