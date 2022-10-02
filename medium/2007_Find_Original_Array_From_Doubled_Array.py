# An integer array original is transformed into a doubled array changed by
# appending twice the value of every element in original, and then randomly
# shuffling the resulting array.
#
# Given an array changed, return original if changed is a doubled array. If
# changed is not a doubled array, return an empty array. The elements in
# original may be returned in any order.

from typing import List
from collections import Counter


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counts = Counter(changed)
        if counts[0] % 2 == 1:
            return []
        for val in sorted(counts):
            if counts[val] > counts[val * 2]:
                return []
            counts[2 * val] -= counts[val] if val else counts[val] // 2
        return list(counts.elements())
