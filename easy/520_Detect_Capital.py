class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        if word[0].isupper():
            flag = word[1].isupper()
            for ch in word[2:]:
                if ch.isupper() != flag:
                    return False
        else:
            for ch in word:
                if ch.isupper():
                    return False
        return True

    def allUpper(self, s: str) -> bool:
        for ch in s:
            if ch.islower():
                return False
        return True

    def allLower(self, s: str) -> bool:
        for ch in s:
            if ch.isupper():
                return False
        return True


if __name__ == "__main__":
    print(Solution().detectCapitalUse("FlaG"))
