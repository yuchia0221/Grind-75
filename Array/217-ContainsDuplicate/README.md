# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/contains-duplicate)!

### [Basic Solution](/Array/217-ContainsDuplicate/basicSolution.py): Brute Force

```python
def containsDuplicate(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

### [Improved Solution](/Array/217-ContainsDuplicate/improvedSolution.py): Sort

```python
def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()
    left, right = 0, 1
    while right < len(nums):
        if nums[left] == nums[right]:
            return True
        else:
            left, right = right, right + 1

    return False
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

### [Optimized Solution](/Array/217-ContainsDuplicate/optimizedSolution.py): Set or Hash Table

```python
def containsDuplicate(nums: List[int]) -> bool:
    memo = set()
    for number in nums:
        if number in memo:
            return True
        else:
            memo.add(number)

    return False
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
