from typing import List, Optional
import heapq


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a min heap
        min_heap = []
        heapq.heapify(min_heap)
        
        # Insert the first element from each linked list into the min heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        # Create a dummy node to store the merged linked list
        dummy = ListNode()
        curr = dummy
        
        # Merge the linked lists by extracting the minimum element from the min heap
        while min_heap:
            val, i = heapq.heappop(min_heap)
            curr.next = ListNode(val)
            curr = curr.next
            
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return dummy.next