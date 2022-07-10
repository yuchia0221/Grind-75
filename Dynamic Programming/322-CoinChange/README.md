# Coin Change

Problem can be found in [here](https://leetcode.com/problems/coin-change)!

### [Solution](/Dynamic%20Programming/322-CoinChange/solution.py): Dynamic Programming

```python
def coinChange(coins: List[int], amount: int) -> int:
    coins_need = [float("inf") for _ in range(amount+1)]
    coins_need[0] = 0
    for i in range(1, amount+1):
        for coin in coins:
            if coin <= i:
                coins_need[i] = min(coins_need[i], coins_need[i-coin]+1)

    return coins_need[-1] if coins_need[-1] != float("inf") else -1
```

Time Complexity: ![O(nm)](<https://latex.codecogs.com/svg.image?\inline&space;O(nm)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), where n is value of $amount$ and m is the length of coins.
