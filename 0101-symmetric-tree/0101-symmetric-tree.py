# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self,p,q):
        if p == None and q == None:
            return True 
        if p == None or q == None or q.val != p.val:
            return False
        return self.compare(p.left,q.right) and self.compare(p.right,q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None :
            return True 
        return self.compare(root.right,root.left)
        