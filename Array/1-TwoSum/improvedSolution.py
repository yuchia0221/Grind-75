class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        memo = {}
        for i, num in enumerate(nums):
            if num in memo:
                return [memo[num], i]

            memo[target - num] = i
