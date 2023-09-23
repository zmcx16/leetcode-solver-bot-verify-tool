import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for lst in lists:
            if lst:
                heapq.heappush(heap, (lst.val, lst))
        dummy = ListNode()
        curr = dummy
        while heap:
            val, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        return dummy.next