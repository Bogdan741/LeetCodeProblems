from typing import List
from functools import lru_cache
import string


# Kadan Algorithm
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        charCost = {}
        for i in range(len(chars)):
            charCost[chars[i]] = vals[i]

        for cost, character in enumerate(string.ascii_lowercase, 1):
            if character not in chars:
                charCost[character] = cost

        currCost = 0
        maxCost = 0
        for i in range(len(s)):
            currCost = max(0, currCost + charCost[s[i]])
            maxCost = max(currCost, maxCost)

        return maxCost


# Naive dp
class Solution1:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        charCost = {}
        for i in range(len(chars)):
            charCost[chars[i]] = vals[i]

        for cost, character in enumerate(string.ascii_lowercase, 1):
            if character not in chars:
                charCost[character] = cost

        @lru_cache(maxsize=None)
        def solve(i):
            if i == 0:
                return 0
            return max(0, solve(i - 1) + charCost[s[i]], solve(i - 1))

        return solve(len(s) - 1)
