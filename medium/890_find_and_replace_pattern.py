from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        self.compiled_words = []

        # Make it inline to work faster
        def compile_word(word):
            counter = 0
            res = ""
            dict = {}
            for ch in word:
                key = dict.get(ch, None)
                if key is None:
                    dict[ch] = counter
                    res += str(counter)
                    counter += 1
                    continue
                else:
                    res += str(key)
            return res

        for idx, word in enumerate(words, 0):
            self.compiled_words.append((idx, compile_word(word)))

        res = []

        print(self.compiled_words)
        compiledPattern = compile_word(pattern)

        for idx, word in self.compiled_words:
            if word == compiledPattern:
                res.append(words[idx])

        return res
