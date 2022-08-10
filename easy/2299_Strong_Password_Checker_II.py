# A password is said to be strong if it satisfies all the following criteria:
#
# It has at least 8 characters.
# It contains at least one lowercase letter.
# It contains at least one uppercase letter.
# It contains at least one digit.
# It contains at least one special character. The special characters are the characters in the following string: "!@#$%^&*()-+".
# It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" does not).
# Given a string password, return true if it is a strong password. Otherwise, return false.
import re


# Using regex (Faster but due to the c regex)
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        flag = False
        while True:
            if len(password) < 8:
                break
            if re.search(r"[A-Z]", password) is None:
                break
            if re.search(r"[a-z]", password) is None:
                break
            if re.search(r"[0-9]", password) is None:
                break
            if re.search(r"[!@#$%^&*()\-+]", password) is None:
                break
            if re.search(r"(.)\1", password):
                break
            flag = True
            break
        return flag


# Without regex
class Solution1:
    def strongPasswordCheckerII(self, p: str) -> bool:
        spl = "!@#$%^&*()-+"
        flag = False
        while True:
            if len(p) >= 8:
                break
            for ch in p:
                if ch.islower():
                    break
            for ch in p:
                if ch.isupper():
                    break
            for ch in p:
                if ch.isnumeric():
                    break
            for ch in p:
                if ch in spl:
                    break
            for m in range(1, len(p)):
                if p[m - 1] == p[m]:
                    break
            flag = True
            break
        return flag
