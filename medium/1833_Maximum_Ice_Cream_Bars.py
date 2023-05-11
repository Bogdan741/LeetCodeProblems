from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        total = 0
        costs.sort()
        for i, cost in enumerate(costs):
            total += cost
            if total > coins:
                return i
        return len(costs)
