# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
#
#     For example, "ACGAATTCCG" is a DNA sequence.
#
# When studying DNA, it is useful to identify repeated sequences within the DNA.
#
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

# TAG: Sliding window

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        window_start = 0
        frequancy_map = {}
        for window_end in range(10, len(s)):
            dna = s[window_start:window_end]
            if dna not in frequancy_map:
                frequancy_map[dna] = 0
            frequancy_map[dna] += 1
            window_start += 1

        return [key for key, value in frequancy_map.items() if value > 1]
