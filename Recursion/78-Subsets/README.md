# Subsets

Problem can be found in [here](https://leetcode.com/problems/subsets)!

### [Solution](/Recursion/78-Subsets/solution.py): Recursion

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output_list = []
        self.dfs(output_list, nums, [], 0)
        return output_list

    def dfs(self, output_list: List[List[int]], nums: List[int], current: List[int], index: int):
        output_list.append(list(current))
        for i in range(index, len(nums)):
            current.append(nums[i])
            self.dfs(output_list, nums, current, i+1)
            current.pop()
```

Time Complexity: ![O(n*2^n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n\cdot&space;2^n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of array $nums$.
