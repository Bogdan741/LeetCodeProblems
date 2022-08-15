# You are given a string s and an array of strings words of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of
# each word in words exactly once, in any order, and without any intervening
# characters.
#
# You can return the answer in any order.

from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        step = len(words[0])
        max_length = step * len(words)
        count = {word: 0 for word in words}
        for i in words:
            count[i] += 1

        res = []

        def help(left):
            dict = {word: 0 for word in words}
            sum = ""
            splittedWord = [
                s[(i - 1) * step + left : i * step + left]
                for i in range(1, len(s) // step + 1)
                if i * step + left <= len(s)
            ]

            for idx, word in enumerate(splittedWord, 0):
                if word not in words:
                    for key in dict:
                        dict[key] = 0
                    sum = ""
                    continue
                dict[word] += 1
                sum += word
                while len(sum) > max_length or dict[word] > count[word]:
                    dict[sum[:step]] -= 1
                    sum = sum[step:]

                flag = True
                for key in dict:
                    if dict[key] != count[key]:
                        flag = False
                        break

                if flag:
                    res.append((idx + 1) * step - max_length + left)

        for i in range(step):
            help(i)
        return res


# The same idea, but better impl
class Solution1:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = collections.Counter(words)

        def sliding_window(left):
            words_found = collections.defaultdict(int)
            words_used = 0
            excess_word = False

            # Do the same iteration pattern as the previous approach - iterate
            # word_length at a time, and at each iteration we focus on one word
            for right in range(left, n, word_length):
                if right + word_length > n:
                    break

                sub = s[right : right + word_length]
                if sub not in word_count:
                    # Mismatched word - reset the window
                    words_found = collections.defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length  # Retry at the next index
                else:
                    # If we reached max window size or have an excess word
                    while right - left == substring_size or excess_word:
                        # Move the left bound over continously
                        leftmost_word = s[left : left + word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1

                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            # This word was the excess word
                            excess_word = False
                        else:
                            # Otherwise we actually needed it
                            words_used -= 1

                    # Keep track of how many times this word occurs in the window
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        # Found too many instances already
                        excess_word = True

                    if words_used == k and not excess_word:
                        # Found a valid substring
                        answer.append(left)

        answer = []
        for i in range(word_length):
            sliding_window(i)

        return answer


if __name__ == "__main__":
    print(Solution().findSubstring("ababababab", ["ababa", "babab"]))
