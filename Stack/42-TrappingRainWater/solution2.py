from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        left_max = right_max = volumne = 0
        while left <= right:
            if left_max <= right_max:
                volumne += max(left_max - height[left], 0)
                left_max = max(left_max, height[left])
                left += 1
            else:
                volumne += max(right_max - height[right], 0)
                right_max = max(right_max, height[right])
                right -= 1

        return volumne
