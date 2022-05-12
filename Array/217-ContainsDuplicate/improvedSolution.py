from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                return True
            else:
                left, right = right, right + 1

        return False
