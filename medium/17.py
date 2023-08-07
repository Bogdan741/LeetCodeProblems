from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def bactrack(partialRes, idx):
            if idx == len(digits):
                res.append(partialRes)
                return
            digit = digits[idx]
            for letter in digitLetters[digit]:
                partialRes.append(letter)
                bactrack(partialRes[:], idx + 1)
                partialRes.pop()

        bactrack([], 0)
        return ["".join(arr) for arr in res if arr]
