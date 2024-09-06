# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:  
        nums = set(nums)  
        while head and head.val in nums:  
            head = head.next  
        
        temp = head  
        curr = head  
        
        while curr:  
            if curr.val in nums:  
                temp.next = curr.next  
            else:  
                temp = curr  
            curr = curr.next  
        return head
    

        