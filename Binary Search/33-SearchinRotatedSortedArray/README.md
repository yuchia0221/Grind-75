# Search in Rotated Sorted Array

Problem can be found in [here](https://leetcode.com/problems/search-in-rotated-sorted-array)!

### [Solution](/Binary%20Search/33-SearchinRotatedSortedArray/solution.py)

```python
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1

    while left <= right:
        # avoid the potential overflow porblem in other programming language, but not including Python
        mid = left + (right-left) // 2
        if nums[mid] == target:
            return mid

        # The left-handed side of mid in nums is ordered
        if nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        # The right-handed side of mid in nums is ordered
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

Explanation: The difference between the typical binary search problem in a sorted array and this problem is that the array may be possibly rotated somewhere in the array. To perform binary search in this problem, we need to check whether the target is in the left-rotated side or right-rotated side. For instance, assume that there is an array A = [3, 4, 5, 6, 7, 0, 1, 2] and our target number is 7. In this case, the left-rotated side is [3, 4, 5, 6, 7] while the right-rotated side is [0, 1, 2]. We need to determine whether the middle of left and right pointers is in the right-rotated or left-rotated side. To find out which side we are, we can simply achieve so by comparing the value of A[left] and A[mid]. If we are in the left-rotated side, search A[left] ~ A [mid] if A[left] <= target < A[mid] else, search right side. If we are in the right-rotated side, search in A[mid] ~ A[right] if A[mid] < target <= A[right] else, search left side.

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
