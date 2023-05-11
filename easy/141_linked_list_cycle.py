# Definition for singly-linked list.
from __future__ import annotations
from typing import Optional, cast


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        hare: Optional[ListNode] = head
        tortoise: Optional[ListNode] = head
        firstIteration: bool = True
        while True:
            if hare == tortoise and not firstIteration:
                return True
            if hare is None or hare.next is None:
                return False
            hare = hare.next.next
            tortoise = cast(ListNode, tortoise.next)
            firstIteration = False
