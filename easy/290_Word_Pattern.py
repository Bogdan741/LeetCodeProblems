class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return True if self.unify(s.split(" ")) == self.unify(pattern) else False

    def unify(self, iterable) -> str:
        res = []
        dp = {}
        last = 0
        for item in iterable:
            if item in dp:
                res.append(dp[item])
            else:
                dp[item] = last
                res.append(last)
                last += 1
        return "".join(map(chr, res))
