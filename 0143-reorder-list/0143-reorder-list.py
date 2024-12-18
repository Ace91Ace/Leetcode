#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def rev(head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        
        c = 0
        curr = head
        while curr:
            curr = curr.next
            c += 1
        
        m1 = head
        h = math.ceil(c / 2) - 1
        c = 0
        curr = head

        while curr and c != h:
            curr = curr.next
            c += 1
        m2 = curr.next
        curr.next = None

        prev = None
        m2 = Solution.rev(m2)

        m1 = head
        while m2:
            nxt1 = m1.next
            nxt2 = m2.next
            m1.next = m2
            m2.next = nxt1
            m1 = nxt1
            m2 = nxt2

        return head
