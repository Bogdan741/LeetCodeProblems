# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
#
#     'a' maps to ".-",
#     'b' maps to "-...",
#     'c' maps to "-.-.", and so on.
#
# For convenience, the full table for the 26 letters of the English alphabet is given below:
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
#
#     For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
#
# Return the number of different transformations among all words we have.

from typing import List
from collections import defaultdict


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mapping = [
            ".-", "-...", "-.-.", "-..", ".", "..-.",
            "--.", "....", "..", ".---", "-.-", ".-..",
            "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--..", ]
        dict = defaultdict(int)
        for word in words:
            encoded = ""
            for ch in word:
                encoded += mapping[ord(ch) - ord('a')]
            dict[encoded] += 1
        return len(dict)
