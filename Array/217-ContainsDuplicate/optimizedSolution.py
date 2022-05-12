from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = set()
        for number in nums:
            if number in memo:
                return True
            else:
                memo.add(number)

        return False
