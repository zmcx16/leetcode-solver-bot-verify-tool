class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node to handle the case where left = 1
        dummy = ListNode(0)
        dummy.next = head
        # Find the node before the left position
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        # Reverse the nodes from left to right
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next