#
# You are given two string arrays words1 and words2.
#
# A string b is a subset of string a if every letter in b occurs in a including
# multiplicity.
#
# For example, "wrr" is a subset of "warrior" but is not a subset of "world". A
# string a from words1 is universal if for every string b in words2, b is a
# subset of a.
#
# Return an array of all the universal strings in words1. You may return the
# answer in any order.
#

class Solution(object):
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord("a")] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans
