# You are given an integer n. We reorder the digits in any order (including the
# original order) such that the leading digit is not zero.
#
# Return true if and only if we can do this so that the resulting number is a
# power of two.

from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = Counter(str(n))
        return any(digits == Counter(str(1 << i)) for i in range(31))
