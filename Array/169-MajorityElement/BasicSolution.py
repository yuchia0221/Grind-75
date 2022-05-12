from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            counter = sum(1 for number in nums if number == nums[i])
            if counter > len(nums) // 2:
                return nums[i]
