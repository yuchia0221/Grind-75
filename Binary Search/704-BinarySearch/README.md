# Binary Search

Problem can be found in [here](https://leetcode.com/problems/binary-search)!

### [Solution](/Binary%20Search/704-BinarySearch/solution.py)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            # target is in the righthand side of mid, so we need to update left
            elif nums[mid] < target:
                left = mid + 1
            # target is in the lefthand side of mid, so we need to update right
            else:
                right = mid - 1

        return -1
```

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
