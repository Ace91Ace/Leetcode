# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        curr = head

        while curr:
            heapq.heappush(heap,curr.val)
            curr = curr.next

        curr= head
        while curr:
            pop = heapq.heappop(heap)
            curr.val = pop
            curr = curr.next
        
        return head
        