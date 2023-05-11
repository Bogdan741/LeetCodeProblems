from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def dfs(index, stage, deq):
            if stage == 4:
                if len(s) == index:
                    res.append(deq[:])
                return

            if index == len(s):
                return

            i = 0
            next = int(s[index: index + i + 1])
            if next == 0:
                deq.append(next)
                dfs(index + i + 1, stage + 1, deq)
                deq.pop(stage)
                return

            while (next >> 8) <= 0 and index + i < len(s):
                deq.append(next)
                dfs(index + i + 1, stage + 1, deq)
                deq.pop(stage)
                i += 1
                next = int(s[index: index + i + 1])

        dfs(0, 0, [])
        return list(map(lambda x: ".".join(map(str, x)), res))


if __name__ == "__main__":
    print(Solution().restoreIpAddresses("25525511135"))
