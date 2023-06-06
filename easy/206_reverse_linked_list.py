from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        if head is None:
            return head
        self.reverse(head)
        return self.head

    def reverse(self, root):
        if root.next is None:
            self.head = root
            return root
        last = self.reverse(root.next)
        last.next = root
        root.next = None
        return root
