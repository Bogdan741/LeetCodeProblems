from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort pairs in ascending order based on the second element.
        pairs.sort(key=lambda x: x[1])
        curr = float("-inf")
        ans = 0

        for pair in pairs:
            if pair[0] > curr:
                ans += 1
                curr = pair[1]
        return ans


class Solution1:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        def longestPairChain(i: int) -> int:
            if memo[i] != 0:
                return memo[i]
            memo[i] = 1
            for j in range(i + 1, n):
                if pairs[i][1] < pairs[j][0]:
                    memo[i] = max(memo[i], 1 + longestPairChain(j))
            return memo[i]

        n = len(pairs)
        pairs.sort()
        memo = [0] * n

        ans = 0
        for i in range(n):
            ans = max(ans, longestPairChain(i))
        return ans
