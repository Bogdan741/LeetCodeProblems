from typing import List
from functools import reduce
from operator import add


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(0, len(points) - 1):
            point1 = points[i]
            point2 = points[i + 1]
            res += self.findTime(point1, point2)
        return res

    def findTime(self, point1, point2):
        dispositionX, dispositionY = abs(point2[0] - point1[0]), abs(
            point2[1] - point1[1]
        )
        return max(dispositionX, dispositionY)
