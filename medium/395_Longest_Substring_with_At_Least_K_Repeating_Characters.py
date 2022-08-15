# Given a string s and an integer k, return the length of the longest substring
# of s such that the frequency of each character in this substring is greater
# than or equal to k.

# TAG: Sliding window, Divide and conquer
from collections import Counter


# O(n^2) - dynamic programming
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        char_count = Counter(s)
        for char, count in char_count.items():
            if count < k:
                mid = 0
                for i in range(len(s)):
                    if s[i] == char:
                        mid = i
                        break
                left = self.longestSubstring(s[:mid], k)
                right = self.longestSubstring(s[mid + 1:], k)

                return max(left, right)
        return len(s)


# Sliding window
# class Solution1:
#     def longestSubstring(self, s: str, k: int) -> int:
#         window_start = 0
#         char_count = Counter(s)
#         maxLen = 0
#         for window_end in range(len(s)):
#             if char_count[window_end] < k:
#
#                 window_start = window_end + 1

if __name__ == "__main__":
    print(Solution().longestSubstring("aaabb", 3))
