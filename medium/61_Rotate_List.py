# Given the head of a linked list, rotate the list to the right by k places.

# TAG: Linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None:
            return None

        # Find length and tail
        n = 1
        tail: ListNode | None = head
        while tail.next:
            n += 1
            tail = tail.next

        # Find shift
        rotation = k % n
        shift = n - rotation - 1
        # Find new tail and new head
        new_tail: ListNode | None = head
        while shift > 0 and new_tail:
            new_tail = new_tail.next
            shift -= 1

        # Change tail and head
        new_head: ListNode | None = new_tail.next if new_tail.next is not None else head
        tail.next = head
        new_tail.next = None
        return new_head
