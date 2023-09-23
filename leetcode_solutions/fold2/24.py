class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(node):
            if not node or not node.next:
                return node
            next_node = node.next
            node.next = swap(next_node.next)
            next_node.next = node
            return next_node
        return swap(head)