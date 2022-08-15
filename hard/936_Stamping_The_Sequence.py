# You are given two strings stamp and target. Initially, there is a string s of
# length target.length with all s[i] == '?'. In one turn, you can place stamp
# over s and replace every letter in the s with the corresponding letter from
# stamp.
#
#     For example, if stamp = "abc" and target = "abcba", then s is "?????"
#     initially. In one turn you can: place stamp at index 0 of s to obtain
#     "abc??", place stamp at index 1 of s to obtain "?abc?", or place stamp at
#     index 2 of s to obtain "??abc". Note that stamp must be fully contained
#     in the boundaries of s in order to stamp (i.e., you cannot place stamp at
#     index 3 of s).
#
# We want to convert s to target using at most 10 * target.length turns.
#
# Return an array of the index of the left-most letter being stamped at each
# turn. If we cannot obtain target from s within 10 * target.length turns,
# return an empty array.

from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def equal(a, b):  # b-> can have '?'
            c = 0
            for i in range(len(a)):
                if a[i] != b[i] and b[i] != "?":
                    return False
                if b[i] == "?":
                    c += 1
            return c < len(b)  # if b has only ?'s, return false,
            # because there is no need to replace it will just increase
            # the output array length and runtime.

        ans = []
        n = len(target)
        tar = "?" * n
        m = len(stamp)
        f = True
        while len(ans) < 10 * n and f and target != tar:
            start = 0
            f = False
            while start + m <= n:
                if equal(stamp, target[start: start + m]):
                    ans.append(start)
                    target = target[:start] + "?" * m + target[start + m:]
                    f = True
                start += 1
        if target == tar:
            return ans[::-1]
        return []
