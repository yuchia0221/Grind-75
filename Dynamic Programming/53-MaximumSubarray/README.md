# Maximum Subarray

Problem can be found in [here](https://leetcode.com/problems/maximum-subarray)!

### [Solution](/Dynamic%20Programming/53-MaximumSubarray/solution.py): Dynamic Programming

```python
def maxSubArray(nums: List[int]) -> int:
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i-1]+nums[i])

    return max(nums)
```

Explanation: Define the maximum value of a given subarray from index 0 to i as P(i) and the original array as nums. We can easily write down the recursion function P(i) = max(nums[i], P(i-1)+nums[i]).

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>), where n is the length of array.
