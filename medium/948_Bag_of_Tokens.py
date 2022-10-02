# You have an initial power of power, an initial score of 0, and a bag of
# tokens where tokens[i] is the value of the ith token (0-indexed).
#
# Your goal is to maximize your total score by potentially playing each token
# in one of two ways:
#
#     If your current power is at least tokens[i], you may play the ith token
#     face up, losing tokens[i] power and gaining 1 score. If your current
#     score is at least 1, you may play the ith token face down, gaining
#     tokens[i] power and losing 1 score.
#
# Each token may be played at most once and in any order. You do not have to
# play all the tokens.
#
# Return the largest possible score you can achieve after playing any number of
# tokens.

from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        res = score = 0
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        while l < r:
            if P - tokens[l] >= 0:
                P -= tokens[l]
                l += 1
                score += 1
                res = max(res, score)
            elif P - tokens[l] < 0 and score > 0:
                P += tokens[r]
                r -= 1
                score -= 1
            else:
                # have no score no power
                break
        return res
