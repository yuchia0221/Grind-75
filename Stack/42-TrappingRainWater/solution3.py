from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volumne = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                candidate = height[stack.pop()]
                if stack:
                    bounded_height = min(height[i], height[stack[-1]]) - candidate
                    width = i - stack[-1] - 1
                    volumne += bounded_height * width

            stack.append(i)

        return volumne
