class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        memo = {}
        for i, j in enumerate(nums):
            number_to_find = target - j
            try:
                return [memo[j], i]
            except KeyError:
                memo[number_to_find] = i
