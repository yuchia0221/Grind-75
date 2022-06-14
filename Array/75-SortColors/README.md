# Sort Colors

Problem can be found in [here](https://leetcode.com/problems/sort-colors)!

### [Solution](/Array/75-SortColors/solution.py): Three Pointers

```python
# 0: red, 1: white, 2: blue
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

Explanation: Use three pointers to perform in-place sorting. If nums[mid] is 0, meaning that we need to swap the value in nums[left] and nums[mid] to make the array sorted. Another case is that if we encounter 2 in nums[mid], we know that we should swap nusmms[right] and nums[mid] to keep the array sorted. By doing so, the array will be sorted in O(n) time after iterating the whole array (worst case).

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
