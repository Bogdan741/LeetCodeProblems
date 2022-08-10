from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        dp = [1] * n
        arr.sort()
        index = {x: i for i, x in enumerate(arr)}
        for i, x in enumerate(arr):
            for left in range(i):
                if x % arr[left] == 0:
                    right = index.get(x // arr[left], None)
                    if right is not None:
                        dp[i] += dp[left] * dp[right]
        return sum(dp) % mod
