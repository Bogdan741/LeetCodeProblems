from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        sum = 0
        for i, num in enumerate(nums, 1):
            sum += num
            prefix_sum[i] = sum
        res = [-1] * n
        for i in range(k, n - k):
            res[i] = (prefix_sum[i + k + 1] - prefix_sum[i - k]) // (2 * k + 1)
        return res
