# Trapping Rain Water

Problem can be found in [here](https://leetcode.com/problems/trapping-rain-water)!

### [Solution](/Stack/42-TrappingRainWater/solution.py): Two Pointers

```python
def trap(height: List[int]) -> int:
    max_left = max_right = volumne = 0
    left, right = 0, len(height)-1
    while left <= right:
        if max_left <= max_right:
            volumne += max(max_left - height[left], 0)
            max_left = max(max_left, height[left])
            left += 1
        else:
            volumne += max(max_right - height[right], 0)
            max_right = max(max_right, height[right])
            right -= 1

    return volumne
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
