from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k) -> Optional[ListNode]:
        self.flag = False
        (last, next) = self.reverseN(head, k)
        while next is not None:
            self.flag = False
            (last1, next1) = self.reverseN(next.next, k)
            next.next = last1
            next = next1
        return last

    def reverseN(self, head: ListNode, n):
        if head is None:
            self.flag = True
            return (head, None)
        if n == 1:
            self.successor = head.next
            return (head, head.next)
        last = self.reverseN(head.next, n - 1)[0]
        if self.flag:
            return (head, None)
        head.next.next = head
        head.next = self.successor
        return (last, head)
