class SolutionOld:
    def countVowelPermutation(self, n: int) -> int:
        if n == 0:
            return 0
        dict = {"a": [1], "e": [1], "i": [1], "o": [1], "u": [1]}
        for i in range(1, n):
            dict["a"].append(dict["e"][i - 1] + dict["u"][i - 1] + dict["i"][i - 1])
            dict["e"].append(dict["a"][i - 1] + dict["i"][i - 1])
            dict["i"].append(dict["o"][i - 1] + dict["e"][i - 1])
            dict["o"].append(dict["i"][i - 1])
            dict["u"].append(dict["o"][i - 1] + dict["i"][i - 1])
        return sum([val[-1] for val in dict.values()])


# Optimized version
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 0:
            return 0
        dict = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        for _ in range(1, n):
            ends_a = dict["a"]
            ends_e = dict["e"]
            ends_i = dict["i"]
            ends_o = dict["o"]
            ends_u = dict["u"]
            dict["a"] = ends_e + ends_u + ends_i
            dict["e"] = ends_a + ends_i
            dict["i"] = ends_o + ends_e
            dict["o"] = ends_i
            dict["u"] = ends_o + ends_i

        return sum([val for val in dict.values()])
