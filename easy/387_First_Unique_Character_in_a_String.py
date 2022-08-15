from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_cout = Counter(s)
        for ch in s:
            if char_cout[ch] == 1:
                return s.find(ch)
        return -1
