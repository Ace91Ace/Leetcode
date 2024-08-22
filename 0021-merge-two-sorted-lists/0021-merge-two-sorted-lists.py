# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        current = list2

        while (current) :
            lis.append(current.val)
            current = current.next
        
        current = list1

        while current:
            lis.append(current.val)
            current = current.next
        
        if not lis:
            return None

        lis.sort()

        head = ListNode(lis[0])
        curr = head
        for i in range(1,len(lis)):
            node = ListNode(lis[i])
            curr.next = node
            curr = curr.next
        return head


        