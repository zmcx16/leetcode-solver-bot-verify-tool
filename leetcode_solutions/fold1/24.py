def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    first = head
    second = head.next
    first.next = self.swapPairs(second.next)
    second.next = first
    return second