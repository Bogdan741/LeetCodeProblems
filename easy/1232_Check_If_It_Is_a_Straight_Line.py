# You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
# represents the coordinate of a point. Check if these points make a straight
# line in the XY plane.

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True
        vectors = [
            (valX - coordinates[0][0], valY - coordinates[0][1])
            for valX, valY in coordinates
        ]
        flag = True
        for i in range(1, len(vectors) - 1):
            # Avoid zero division for duplicate points
            if vectors[i + 1][0] == 0 or vectors[i + 1][1] == 0:
                if (vectors[i][0] == 0 and vectors[i + 1][0] == 0) or (
                    vectors[i][1] == 0 and vectors[i + 1][1] == 0
                ):
                    continue
                flag = False
                break
            if vectors[i][0] / vectors[i + 1][0] != vectors[i][1] / vectors[i + 1][1]:
                flag = False
                break

        return flag
