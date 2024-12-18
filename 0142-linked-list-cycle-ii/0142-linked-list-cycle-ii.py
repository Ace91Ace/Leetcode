# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None :
            return None
            
        sp = head
        fp = head

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            if fp == sp:
                break
        else:
            return None
    
        curr = head
        while curr != sp:
            curr = curr.next
            sp = sp.next
        return curr
