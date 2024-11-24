# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head.next
        prev = head
        head = temp

        while temp:
            x = temp.next
            temp.next = prev
            if not x or not x.next:
                prev.next = x
                break
            prev.next = x.next
            prev = x
            temp = prev.next

        return head
