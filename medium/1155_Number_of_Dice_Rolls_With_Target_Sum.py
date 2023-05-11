# You have n dice and each die has k faces numbered from 1 to k.
#
# Given three integers n, k, and target, return the number of possible ways
# (out of the kn total ways) to roll the dice so the sum of the face-up numbers
# equals target. Since the answer may be too large, return it modulo 109 + 7.

from functools import lru_cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.dp(n, k, target)

    @lru_cache(maxsize=None)
    def dp(self, dice: int, k: int, target: int) -> int:
        if target < 0:
            return 0
        if dice == 0:
            return 1 if target == 0 else 0
        res = 0
        dice -= 1
        for i in range(k):
            res += self.dp(dice, k, target - i - 1)
        return res % (1_000_000_000 + 7)
