class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseGroup(head, tail):
            prev = None
            curr = head
            while curr != tail:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head
        reversed_head = reverseGroup(head, curr)
        head.next = self.reverseKGroup(curr, k)
        return reversed_head