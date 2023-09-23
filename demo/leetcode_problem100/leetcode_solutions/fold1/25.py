def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reverseGroup(curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = curr
        count = 0
        while node and count < k:
            node = node.next
            count += 1
        if count == k:
            prev = None
            next_node = None
            curr = curr
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            if next_node:
                head.next = reverseGroup(next_node, k)
            return prev
        return curr
    return reverseGroup(head, k)