from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_need = [float("inf") for _ in range(amount+1)]
        coins_need[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    coins_need[i] = min(coins_need[i], coins_need[i-coin]+1)

        return coins_need[-1] if coins_need[-1] != float("inf") else -1
