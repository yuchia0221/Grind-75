# Permutations

Problem can be found in [here](https://leetcode.com/problems/permutations)!

### [Solution](/Recursion/46-Permutations/solution.py): Recursion

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output_list = []
        visited_numbers = set()
        self.dfs(nums, output_list, visited_numbers, [])
        return output_list

    def dfs(self, nums: List[int], output_list: List[List[int]], visited_numbers: Set[int], tempt: List[int]) -> None:
        if len(tempt) == len(nums):
            output_list.append(tempt[:])
            return

        for number in nums:
            if number not in visited_numbers:
                visited_numbers.add(number)
                tempt.append(number)
                self.dfs(nums, output_list, visited_numbers, tempt)
                tempt.pop()
                visited_numbers.remove(number)
```

Time Complexity: ![O(n*n!)](<https://latex.codecogs.com/svg.image?\inline&space;O(n*n!)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is the length of array $nums$.
