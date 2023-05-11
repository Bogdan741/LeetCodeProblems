from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = 0
        cprefix_sum = 0
        total = 0
        for i in range(len(gas)):
            cprefix_sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if cprefix_sum < 0:
                idx = i + 1
                cprefix_sum = 0

        if idx == len(gas) or total < 0:
            return -1
        return idx
