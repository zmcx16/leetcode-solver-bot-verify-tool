class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = less = ListNode(0)
        greater_head = greater = ListNode(0)
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next
        less.next = greater_head.next
        greater.next = None
        return less_head.next