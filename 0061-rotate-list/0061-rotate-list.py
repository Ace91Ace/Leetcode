# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:  
            return head
        curr = head
        l = 1
        while curr.next:
            curr = curr.next
            l += 1
        curr.next = head

        k  = k % l

        y = head
        for i in range(l-k-1):
            y = y.next
        n = y.next
        y.next = None

        return n

