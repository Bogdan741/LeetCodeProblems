from collections import Counter

# O(nlogn)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# O(n)
class BetterSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
