# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_l(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        revlis = reverse_l(head)
        
        carry = 0
        curr = revlis

        while curr:
            x = curr.val*2 + carry
            if x > 9:
                x = x - 10
                carry = 1
            else:
                carry = 0
            curr.val = x
            curr = curr.next
        head = reverse_l(revlis)

        
        if carry :
            h = ListNode(carry)
            h.next = head
            head = h
        return head