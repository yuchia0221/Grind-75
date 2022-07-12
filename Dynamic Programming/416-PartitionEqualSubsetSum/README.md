# Partition Equal Subset Sum

Problem can be found in [here](https://leetcode.com/problems/partition-equal-subset-sum)!

### [Solution 1](/Dynamic%20Programming/416-PartitionEqualSubsetSum/solution1.py): Dynamic Programming + Tabulation

```python
def canPartition(nums: List[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False

    half_sum = total_sum // 2
    memo = [True] + [False]*half_sum
    for num in nums:
        for j in range(half_sum, num-1, -1):
            memo[j] |= memo[j-num]

    return memo[half_sum]
```

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(m)](<https://latex.codecogs.com/svg.image?\inline&space;O(m)>), where n is the length of array and m is the sum of array.

### [Solution 2](/Dynamic%20Programming/416-PartitionEqualSubsetSum/solution2.py): Dynamic Programming + Bitwise Operations

```python
def canPartition(nums: List[int]) -> bool:
    total_sum = sum(nums)
    if total_sum % 2 == 0:
        return False

    half_sum, bit = total_sum // 2, 1
    for num in nums:
        bit |= bit << num

    return bit & 1 << half_sum
```

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(m)](<https://latex.codecogs.com/svg.image?\inline&space;O(m)>), where n is the length of array and m is the sum of array.
