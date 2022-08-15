# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.

# TAG: Sliding window

from typing import List
from collections import defaultdict, Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagramLen = len(p)
        window_start = 0
        chars_found = defaultdict(int)
        count = Counter(p)
        excess_char = False
        chars_count = 0

        res = []
        for window_end in range(len(s)):
            ch = s[window_end]
            if ch not in p:
                chars_found = defaultdict(int)
                chars_count = 0
                window_start = window_end + 1
                continue

            chars_found[ch] += 1
            chars_count += 1
            if chars_found[ch] > count[ch]:
                excess_char = True

            while window_end - window_start > anagramLen or excess_char:
                lastCh = s[window_start]
                window_start += 1
                chars_found[lastCh] -= 1
                chars_count -= 1
                if lastCh == ch:
                    excess_char = False

            if chars_count == anagramLen:
                res.append(window_start)

        return res


if __name__ == "__main__":
    print(Solution().findAnagrams("cbababacd", "abc"))
