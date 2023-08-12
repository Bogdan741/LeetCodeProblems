from functools import lru_cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(key=lambda x: -x)

        @lru_cache(maxsize=None)
        def solve(amount, current):
            if amount < 0:
                return 0
            if amount == 0:
                return 1

            res = 0
            for idx in range(current, len(coins)):
                coin = coins[idx]
                i = 1
                while amount - i * coin >= 0:
                    res += solve(amount - i * coin, idx + 1)
                    i += 1
            return res

        return solve(amount, 0)


class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(n - 1, -1, -1):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]

        return dp[amount]
