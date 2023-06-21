from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        dp = {}
        sum = 0
        prefix_sum = [0] * (len(stoneValue) + 1)
        for i, num in enumerate(stoneValue, 1):
            sum += num
            prefix_sum[i] = sum

        def solve(start, end):
            if (start, end) in dp:
                return dp[(start, end)]
            if end - start == 1:
                return 0

            res = 0
            for i in range(start + 1, end):
                right = prefix_sum[end] - prefix_sum[i]
                left = prefix_sum[i] - prefix_sum[start]
                if right > left:
                    res = max(res, left + solve(start, i))
                elif right < left:
                    res = max(res, right + solve(i, end))
                else:
                    res = max(res, right + solve(i, end), left + solve(start, i))
            dp[(start, end)] = res
            return res

        res = solve(0, len(stoneValue))
        return res
