# Definition for singly-linked list.
from __future__ import annotations
from typing import Optional, cast


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head) -> Optional[ListNode]:
        if head is None:
            return None

        hare = head
        tortoise = head
        while hare is not None and hare.next is not None:
            hare = hare.next.next
            tortoise = tortoise.next
            if tortoise == hare:
                tortoise = head
                while tortoise != hare:
                    tortoise = tortoise.next
                    hare = hare.next
                return tortoise
        return None
