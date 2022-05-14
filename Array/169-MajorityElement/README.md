# Majority Element

Problem can be found in [here](https://leetcode.com/problems/majority-element/)!

### [Basic Solution](/Array/169-MajorityElement/BasicSolution.py): Brute Force

```python
def majorityElement(nums: List[int]) -> int:
    for i in range(len(nums)):
        counter = sum(1 for number in nums if number == nums[i])
        if counter > len(nums) // 2:
            return nums[i]
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

### [Improved Solution](/Array/169-MajorityElement/ImprovedSolution.py): Hash Table

```python
def majorityElement(nums: List[int]) -> int:
    memo = {}
    threshold = len(nums) // 2
    for number in nums:
        try:
            memo[number] += 1
        except KeyError:
            memo[number] = 1

        if memo[number] > threshold:
                return number
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
