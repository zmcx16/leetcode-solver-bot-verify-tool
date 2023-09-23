class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        less_ptr = less_head
        greater_ptr = greater_head
        curr = head
        while curr:
            if curr.val < x:
                less_ptr.next = curr
                less_ptr = less_ptr.next
            else:
                greater_ptr.next = curr
                greater_ptr = greater_ptr.next
            curr = curr.next
        less_ptr.next = greater_head.next
        greater_ptr.next = None
        return less_head.next