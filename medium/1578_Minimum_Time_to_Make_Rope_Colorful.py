# Alice has n balloons arranged on a rope. You are given a 0-indexed string
# colors where colors[i] is the color of the ith balloon.
#
# Alice wants the rope to be colorful. She does not want two consecutive
# balloons to be of the same color, so she asks Bob for help. Bob can remove
# some balloons from the rope to make it colorful. You are given a 0-indexed
# integer array neededTime where neededTime[i] is the time (in seconds) that
# Bob needs to remove the ith balloon from the rope.
#
# Return the minimum time Bob needs to make the rope colorful.

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        cur_max_time = 0
        for i in range(len(colors)):
            if i > 0 and colors[i - 1] != colors[i]:
                # Start new group
                cur_max_time = 0
            total += min(cur_max_time, neededTime[i])
            cur_max_time = max(cur_max_time, neededTime[i])
        return total
