from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.solve(head)

    def solve(self, node):
        if node is not None and node.next is not None:
            first = node.next
            node.next = self.solve(first.next)
            first.next = node
            return first
        return node
