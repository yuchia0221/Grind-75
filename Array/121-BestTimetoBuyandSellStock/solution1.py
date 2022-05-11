from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxGap = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[left] < prices[right]:
                maxGap = max(maxGap, prices[right] - prices[left])
                right += 1
            else:
                left, right = right, right + 1

        return maxGap
