from typing import Optional  

class ListNode:  
    def __init__(self, value=0, next=None):  
        self.value = value  
        self.next = next  

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
        
        k = k % l  
        
        steps_to_new_tail = l - k  
        y = head  
        for _ in range(steps_to_new_tail - 1):  
            y = y.next  
            
        nh = y.next  
        y.next = None  
        
        return nh