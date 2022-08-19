# Best Time to Buy and Sell Stock

Problem can be found in [here](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)!

### [Solution 1](/Array/121-BestTimetoBuyandSellStock/solution1.py): Left Right Pointer

```python
 def maxProfit(prices: List[int]) -> int:
    maxGap = 0
    left, right = 0, 1
    while right < len(prices):
        if prices[left] < prices[right]:
            maxGap = max(maxGap, prices[right] - prices[left])
            right += 1
        else:
            left, right = right, right + 1

    return maxGap
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

Explanation: We cannot buy a stock in the future and sell it now in stock market; thus, we only need to store the lowest stock price in every iteration. And in next iteration, we only need to check whether current stock price is higher than previous lowest stock price. If so, then we might need to update _maxGap_. On the other hand, if current stock price is lower than previous lowest price, then we need to update two pointers (_left_, _right_).

### [Solution 2](/Array/121-BestTimetoBuyandSellStock/solution2.py): Min Max

```python
def maxProfit(prices: List[int]) -> int:
    buyPrice, maxGap = float("inf"), 0
    for price in prices:
        buyPrice, maxGap = min(buyPrice, price), max(maxGap, price - buyPrice)

    return maxGap
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

Explanation: Instead of using two variables to store the index of the lowest and current price of stock like [solution 1](#solution-1array121-besttimetobuyandsellstocksolution1py-left-right-pointer), we only need to store the lowest price as iteration goes on. If we find current price is less than pervious lowest price, then it is possible that the maximum profit might change. Therefore, we might need to update the value of _maxGap_ as shown in the code section above.
