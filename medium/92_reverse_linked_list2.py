from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: ListNode, left: int, right: int
    ) -> Optional[ListNode]:
        self.successor = None
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head: ListNode, n):
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last


# def reverse(head):
#     if (head.next is None):
#         return head
#     last = reverse(head.next)
#     head.next.next = head
#     head.next = None
#     return last


# if __name__ == "__main__":
#     a = ListNode(5, ListNode(4, ListNode(3, ListNode(2))))
#     reverse(a)
#     print(a)
