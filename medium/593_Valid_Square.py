# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return
# true if the four points construct a square.
#
# The coordinate of a point pi is represented as [xi, yi]. The input is not
# given in any order.
#
# A valid square has four equal sides with positive length and four equal
# angles (90-degree angles).
import math
from functools import cmp_to_key
from typing import List


class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        def length(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        polygon = [p1, p2, p3, p4]
        polygon.sort(
            key=cmp_to_key(lambda x, y: x[1] - y[1] if x[0] == y[0] else x[0] - y[0])
        )
        return (
            length(polygon[0], polygon[1]) > 0
            and length(polygon[0], polygon[1]) == length(polygon[0], polygon[2])
            and length(polygon[0], polygon[2]) == length(polygon[1], polygon[3])
            and length(polygon[1], polygon[3]) == length(polygon[2], polygon[3])
            and length(polygon[0], polygon[3]) == length(polygon[1], polygon[2])
        )
