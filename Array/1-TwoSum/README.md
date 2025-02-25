# Two Sum

The Two Sum problem is a classic algorithmic challenge where we need to find two numbers in an array that sum up to a given target value. You can find the full problem description [here](https://leetcode.com/problems/two-sum/)!

### [Basic Solution](/Array/1-TwoSum/basicSolution.py): Brute Force

```python
def twoSum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        number_to_find = target - nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == number_to_find:
                return [i, j]
```

Time Complexity: $O(n^2)$, Space Complexity: $O(1)$

Explanation: This brute-force solution iterates through each element and checks all subsequent elements to find a pair that sums to the target. Since we check all pairs, the time complexity is $O(n^2)$.

### [Improved Solution](/Array/1-TwoSum/improvedSolution.py): Hash Table

```python
def twoSum(self, nums: list, target: int) -> list:
    memo = {}
    for i, num in enumerate(nums):
        if num in memo:
            return [memo[num], i]

        memo[target - num] = i
```

Time Complexity: $O(n)$, Space Complexity: $O(n)$

Explanation: Instead of performing a brute-force search through the array, this solution uses a hash table (dictionary) to store the difference between the target and each element. This allows us to check if the required complement exists in $O(1)$ time, reducing the overall complexity to
$O(n)$.
