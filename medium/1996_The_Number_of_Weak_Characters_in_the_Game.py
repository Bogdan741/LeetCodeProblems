# You are playing a game that contains multiple characters, and each of the
# characters has two main properties: attack and defense. You are given a 2D
# integer array properties where properties[i] = [attacki, defensei] represents
# the properties of the ith character in the game.
#
# A character is said to be weak if any other character has both attack and
# defense levels strictly greater than this character's attack and defense
# levels. More formally, a character i is said to be weak if there exists
# another character j where attackj > attacki and defensej > defensei.
#
# Return the number of weak characters.

from typing import List
from functools import cmp_to_key
import math


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=cmp_to_key(type(self).compare))
        res = 0
        max_def = -math.inf
        for _, defense in properties:
            res += defense < max_def
            max_def = max(defense, max_def)

        return res

    @staticmethod
    def compare(x, y):
        if x[0] == y[0]:
            return x[1] - y[1]
        return y[0] - x[0]
