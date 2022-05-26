from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = max_right = volumne = 0
        left, right = 0, len(height)-1
        while left <= right:
            if max_left <= max_right:
                volumne += max(max_left - height[left], 0)
                max_left = max(max_left, height[left])
                left += 1
            else:
                volumne += max(max_right - height[right], 0)
                max_right = max(max_right, height[right])
                right -= 1

        return volumne
