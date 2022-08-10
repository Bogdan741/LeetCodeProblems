# Given a string s, find the length of the longest substring without repeating
# characters.

# TAG: Hash table, String, Sliding window

# Time: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = res = 0
        usedChar = {}
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                res = max(res, i - start + 1)
            usedChar[s[i]] = i
        return res
