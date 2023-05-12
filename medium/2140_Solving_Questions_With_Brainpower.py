from typing import List
from functools import lru_cache


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def solve(curr):
            if curr >= len(questions):
                return 0
            return max(
                solve(curr + questions[curr][1] + 1) + questions[curr][0],
                solve(curr + 1),
            )

        return solve(0)


class Solution1:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        dp[-1] = questions[-1][0]
        
        for i in range(n - 2, -1, -1):
            dp[i] = questions[i][0]
            skip = questions[i][1]
            if i + skip + 1 < n:
                dp[i] += dp[i + skip + 1]

            # dp[i] = max(solve it, skip it)
            dp[i] = max(dp[i], dp[i + 1])
        
        return dp[0]
