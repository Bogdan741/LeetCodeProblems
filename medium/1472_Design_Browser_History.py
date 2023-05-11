class BrowserHistory:
    def __init__(self, homepage: str):
        self._historyList = [homepage]
        self._historyEnd = len(self._historyList)
        self._historyPosition = 0

    def visit(self, url: str) -> None:
        self._historyPosition += 1
        self._historyEnd = self._historyPosition + 1
        if self._historyPosition < len(self._historyList):
            self._historyList[self._historyPosition] = url
        else:
            self._historyList.append(url)

    def back(self, steps: int) -> str:
        self._historyPosition = max(self._historyPosition - steps, 0)
        return self._historyList[self._historyPosition]

    def forward(self, steps: int) -> str:
        self._historyPosition = min(self._historyPosition + steps, self._historyEnd - 1)
        return self._historyList[self._historyPosition]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
