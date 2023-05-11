# You are given an array of strings arr. A string s is formed by the
# concatenation of a subsequence of arr that has unique characters.
#
# Return the maximum possible length of s.
#
# A subsequence is an array that can be derived from another array by deleting
# some or no elements without changing the order of the remaining elements.

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # bit_masks = []
        # for word in arr:
        #     mask = 0
        #     for chr in word:
        #         mask |= 1 << (ord(chr) - ord("a"))
        #     bit_masks.append(mask)
        #
        # res = 0
        # for mask in bit_masks:
        #     res |= mask
        #
        # ones = 0
        #
        # while res > 0:
        #     ones += res & 1
        #     res >>= 1
        # return ones
