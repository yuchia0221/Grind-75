# Best Time to Buy and Sell Stock

Problem can be found in [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)!

### [Solution 1](/Array/121-BestTimetoBuyandSellStock/solution1.py): Left Right Pointer

```python
def maxProfit(prices: list[int]) -> int:
    max_gap = 0
    left, right = 0, 1
    while right < len(prices):
        if prices[left] < prices[right]:
            max_gap = max(max_gap, prices[right] - prices[left])
            right += 1
        else:
            left, right = right, right + 1

    return max_gap
```

Time Complexity: $O(n)$, Space Complexity: $O(1)$

Explanation:
Since we cannot buy a stock in the future and sell it in the past, we only need to track the lowest stock price encountered so far. In each iteration, we:

-   Check if the current stock price is higher than the previously recorded lowest price. If so, we update `max_gap` (the maximum profit).
-   If the current stock price is lower than the previous lowest price, we update both pointers (`left` and `right`) to continue scanning for a new minimum price.

### [Solution 2](/Array/121-BestTimetoBuyandSellStock/solution2.py): Min Max

```python
def maxProfit(prices: List[int]) -> int:
    buy_price, max_gap = float("inf"), 0
    for price in prices:
        buy_price = min(buy_price, price)
        max_gap = max(max_gap, price - buy_price)

    return max_gap
```

Time Complexity: $O(n)$, Space Complexity: $O(1)$

Explanation:
Instead of maintaining two separate indices to track the lowest and current stock prices (as done in [Solution 1](#solution-1array121-besttimetobuyandsellstocksolution1py-left-right-pointer)), this approach keeps only one variable, `buy_price`, to store the lowest price encountered so far.

-   If the current stock price is lower than `buy_price`, we update `buy_price`.
-   Otherwise, we check whether selling at the current price would yield a greater profit and update `max_gap` accordingly.

This method is more concise and avoids the need for explicit pointer manipulation.
