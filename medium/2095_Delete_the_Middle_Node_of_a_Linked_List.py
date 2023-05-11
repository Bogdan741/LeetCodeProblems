class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = head
        tmp = slow
        fast = head
        while fast is not None and fast.next:
            fast = fast.next.next
            tmp = slow
            slow = slow.next

        tmp.next = slow.next
        return head
