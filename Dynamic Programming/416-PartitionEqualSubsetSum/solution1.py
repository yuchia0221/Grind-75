from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False

        half_sum = total_sum // 2
        memo = [True] + [False]*half_sum
        for num in nums:
            for j in range(half_sum, num-1, -1):
                memo[j] |= memo[j-num]

        return memo[half_sum]
