from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memo = {}
        threshold = len(nums) // 2
        for number in nums:
            try:
                memo[number] += 1
            except KeyError:
                memo[number] = 1
                
            if memo[number] > threshold:
                    return number
