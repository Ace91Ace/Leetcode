# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = head
        s = head
        flag = 0

        while s and f and f.next:
            if s is  f and flag:
                return True 
            flag = 1

            if s :
                s = s.next
            if f.next:
                f = f.next.next
        return False