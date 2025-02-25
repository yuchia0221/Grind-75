class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price, max_gap = float("inf"), 0
        for price in prices:
            buy_price = min(buy_price, price)
            max_gap = max(max_gap, price - buy_price)

        return max_gap
