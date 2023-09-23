class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = {}
        curr = head

        # Count the frequency of each number
        while curr:
            if curr.val in freq:
                freq[curr.val] += 1
            else:
                freq[curr.val] = 1
            curr = curr.next

        # Remove nodes with frequency greater than 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr:
            if freq[curr.val] > 1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        # Reconstruct the linked list
        result = dummy.next
        result = sorted(result, key=lambda x: x.val)

        return result