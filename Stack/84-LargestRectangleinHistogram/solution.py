from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        largest_area = 0
        heights.append(-1)

        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                current_height = heights[stack.pop()]
                current_width = index - stack[-1] - 1
                current_area = current_height * current_width
                largest_area = max(current_area, largest_area)

            stack.append(index)

        return largest_area
