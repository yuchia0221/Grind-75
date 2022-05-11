from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice, maxGap = float("inf"), 0
        for price in prices:
            buyPrice, maxGap = min(buyPrice, price), max(maxGap, price - buyPrice)

        return maxGap
