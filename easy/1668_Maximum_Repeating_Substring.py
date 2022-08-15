# For a string sequence, a string word is k-repeating if word concatenated k
# times is a substring of sequence. The word's maximum k-repeating value is the
# highest value k where word is k-repeating in sequence. If word is not a
# substring of sequence, word's maximum k-repeating value is 0.
#
# Given strings sequence and word, return the maximum k-repeating value of word
# in sequence.


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        max_rep = (n // m) * word
        kmp = self.kmpTable(max_rep)
        # To work with sequence < word and remove checking out of boundary
        max_rep += "#"

        idx = 0
        res = 0
        for i in range(len(sequence)):
            while idx > 0 and sequence[i] != max_rep[idx]:
                idx = kmp[idx - 1]
            if max_rep[idx] == sequence[i]:
                idx += 1
                res = max(res, idx)
        return res // m

    def kmpTable(self, s: str):
        kmp = [0] * len(s)

        for i in range(1, len(s)):
            idx = kmp[i - 1]
            while idx > 0 and s[idx] != s[i]:
                idx = kmp[idx - 1]  # trace backwards to find the last matching char
            if s[i] == s[idx]:  # matches next
                idx += 1
            kmp[i] = idx

        return kmp
