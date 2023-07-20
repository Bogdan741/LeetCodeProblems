class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal = 0
        res = 0
        for ch in s:
            if ch == ")":
                bal -= 1
            elif ch == "(":
                bal += 1

            if bal == -1:
                res += 1
                bal = 0
        return res + bal


class Solution1:
    def minAddToMakeValid(self, s: str) -> int:
        bal = 0
        res = 0
        for ch in s:
            bal += 81 - ord(ch) * 2

            if bal == -1:
                res += 1
                bal = 0
        return res + bal
