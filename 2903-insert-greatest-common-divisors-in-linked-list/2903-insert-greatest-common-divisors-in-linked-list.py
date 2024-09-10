# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        if not head or not head.next:  
            return head  

        t1 = head  
        t2 = head.next  

        nhead = ListNode(0)  
        ncurr = nhead  

        while t2:  
            ncurr.next = ListNode(t1.val)  
            ncurr = ncurr.next  
            
            
            gcd_value = math.gcd(t1.val, t2.val)  
            ncurr.next = ListNode(gcd_value)   
            ncurr = ncurr.next   
            
             
            t1 = t1.next  
            t2 = t2.next  

        ncurr.next = t1 
        
        return nhead.next 

        