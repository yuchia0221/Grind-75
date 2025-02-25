class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_gap = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[left] < prices[right]:
                max_gap = max(max_gap, prices[right] - prices[left])
                right += 1
            else:
                left, right = right, right + 1

        return max_gap
