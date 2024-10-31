"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:  
    def connect(self, root):  
        r = root  
        while root and root.left:  
            next_node = root.left  
            while root:  
                root.left.next = root.right  
                root.right.next = root.next.left if root.next else None  
                root = root.next  
            root = next_node  
        return r 
        