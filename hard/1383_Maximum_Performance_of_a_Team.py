# You are given two integers n and k and two integer arrays speed and
# efficiency both of length n. There are n engineers numbered from 1 to n.
# speed[i] and efficiency[i] represent the speed and efficiency of the ith
# engineer respectively.
#
# Choose at most k different engineers out of the n engineers to form a team
# with the maximum performance.
#
# The performance of a team is the sum of their engineers' speeds multiplied by
# the minimum efficiency among their engineers.
#
# Return the maximum performance of this team. Since the answer can be a huge
# number, return it modulo 109 + 7.

from typing import List
import heapq


class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        h = []
        res = sSum = 0
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(h, s)
            sSum += s
            if len(h) > k:
                sSum -= heapq.heappop(h)
            res = max(res, sSum * e)
        return res % (10**9 + 7)
