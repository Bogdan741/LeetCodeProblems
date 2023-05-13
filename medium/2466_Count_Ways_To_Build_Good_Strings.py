# Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:
#
#     Append the character '0' zero times.
#     Append the character '1' one times.
#
# This can be performed any number of times.
#
# A good string is a string constructed by the above process having a length between low and high (inclusive).
#
# Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Use dp[i] to record to number of good strings of length i.
        dp = [1] + [-1] * (high)
        mod = 10**9 + 7

        # Find the number of good strings of length `end`.
        def dfs(end):
            if dp[end] != -1:
                return dp[end]
            count = 0
            if end >= zero:
                count += dfs(end - zero)
            if end >= one:
                count += dfs(end - one)
            dp[end] = count % mod
            return dp[end]

        # Add up the number of strings with each valid length [low ~ high].
        return sum(dfs(end) for end in range(low, high + 1)) % mod


class Solution1:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Use dp[i] to record to number of good strings of length i.
        dp = [1] + [-1] * (high)
        mod = 10**9 + 7

        for i in range(1, high + 1):
            if i - zero >= 0 and i - one >= 0:
                dp[i] = (dp[i - zero] + dp[i - one]) % mod
            elif i - zero >= 0:
                dp[i] = dp[i - zero] % mod
            elif i - one >= 0:
                dp[i] = dp[i - one] % mod
            else:
                dp[i] = 0

        return sum(dp[low:]) % mod
