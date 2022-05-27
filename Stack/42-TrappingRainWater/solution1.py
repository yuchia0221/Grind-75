from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        volumne = 0
        left_max, right_max = [0], [0]*len(height)
        left_max[0], right_max[-1] = height[0], height[-1]

        for i in range(1, len(height)):
            left_max.append(max(left_max[-1], height[i]))

        for i in range(len(height)-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        for i in range(len(height)):
            volumne += min(left_max[i], right_max[i]) - height[i]

        return volumne
