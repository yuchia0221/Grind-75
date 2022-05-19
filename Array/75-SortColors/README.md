# Sort Colors

Problem can be found in [here](https://leetcode.com/problems/sort-colors)!

### [Solution](/Array/75-SortColors/solution.py): Three Pointers

```python
def sortColors(nums: List[int]) -> None:
    left, mid, right = 0, 0, len(nums)-1
    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 2:
            nums[right], nums[mid] = nums[mid], nums[right]
            right -= 1
        else:
            mid += 1
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
