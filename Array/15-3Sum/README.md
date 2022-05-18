# 3Sum

Problem can be found in [here](https://leetcode.com/problems/3sum)!

### [Solution](/Array/15-3Sum/solution.py)

```python
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    output_list = []

    for i in range(len(nums)):
        # Since nums are sorted ascendingly,
        # if nums[i] > 0, then nums[i+1:] are all larger than 0.
        # Thus, we do not need to check the sum of any triplet equals 0.
        if nums[i] > 0:
            break

        # We do not need to check duplicate triplet
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]                      # We need to find the sum of two non-duplicate numbers equal target
        left, right = i + 1, len(nums) - 1     # i+1 <= Search range <= len(nums)-1, previous numbers are searched

        while left < right:
            total = nums[left] + nums[right]
            # Case 1: find unique triplet that adds up to 0
            if target == total:
                output_list.append([nums[i], nums[left], nums[right]])
                left += 1

                # Drop duplicated triplet
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
            # Case 2: target is bigger than total => we need to make total smaller through moving the right pointer
            elif target < total:
                right -= 1
            # Case 3: target is smaller than total => we need to make total bigger through moving the left pointer
            else:
                left += 1

    return output_list
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)
