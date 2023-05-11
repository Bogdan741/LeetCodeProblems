# Too naive approuch
from typing import List, Dict


class Solution:
    def groupAnagrams(self, strs: List[str]):
        dict = {}
        for word in strs:
            tmp = "".join(sorted(word))
            if tmp in dict:
                dict[tmp].append(word)
            else:
                dict[tmp] = [word]

        return dict.values()
