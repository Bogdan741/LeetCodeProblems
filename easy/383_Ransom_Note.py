# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        ransomNote_count = Counter(ransomNote)
        flag = True
        for letter, r_count in ransomNote_count.items():
            if letter in count:
                if r_count > count[letter]:
                    flag = False
                    break
            else:
                flag = False
                break
        return flag
