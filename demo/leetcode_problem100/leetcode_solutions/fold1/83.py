class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        unique = set()

        while head:
            if head.val not in unique:
                unique.add(head.val)
                prev.next = head
                prev = head
            else:
                prev.next = head.next

            head = head.next

        prev.next = None

        return dummy.next