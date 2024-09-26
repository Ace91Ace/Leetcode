class Solution:  
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:  
        if not head:  
            return None  
          
        l = 0  
        curr = head  
        while curr:  
            l += 1  
            curr = curr.next  
        curr = head  

        if n == l:  
            return head.next  
        
        for i in range(l - n - 1):  
            curr = curr.next  
        curr.next = curr.next.next  
        
        return head