# Container With Most Water

Problem can be found in [here](https://leetcode.com/problems/container-with-most-water)!

### [Solution](/Array/11-ContainerWithMostWater/solution.py): Two Pointers

```python
def maxArea(height: List[int]) -> int:
    max_volume = 0
    left, right = 0, len(height) - 1

    while left != right:
        # if height[left] is smaller, the only way to increase volume is to check whether
        # moving left to left + 1 increase the volume since width is getting smaller.
        if height[left] >= height[right]:
            volume = height[right] * (right - left)
            right -= 1
        else:
            volume = height[left] * (right - left)
            left += 1

        max_volume = max(max_volume, volume)
    return max_volume
```

Explanation: Sorting intervals can make sure that for any 0 <= i <= size of intervals-1, intervals\[i][0]<=intervals\[i+1][0], which is a great property that we only need to change end time in overlapping cases.

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
