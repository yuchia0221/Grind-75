# Two Sum

Problem can be found in [here](https://leetcode.com/problems/two-sum/)!

### [Basic Solution](/Array/1-TwoSum/basicSolution.py): Brute Force

```python
# target: int, nums: List[int]

 for i in range(len(nums)):
    number_to_find = target - nums[i]
    for j in range(i + 1, len(nums)):
        if nums[j] == number_to_find:
            return [i, j] # Find indices of the two numbers!
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

Explanation: Simply iterate the array and find the target value among the array in each iteration.

### [Improved Solution](/Array/1-TwoSum/improvedSolution.py): Hash Table

```python
memo = {}
for i, j in enumerate(nums):
    number_to_find = target - j
    try:
        return [memo[j], i] # Find indices of the two numbers!
    except KeyError:
        memo[number_to_find] = i
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

Explanation: Instead of searching the whole array blindlessly in each iteration, using a hash table can determine whether this element is the target value in ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>) time.
