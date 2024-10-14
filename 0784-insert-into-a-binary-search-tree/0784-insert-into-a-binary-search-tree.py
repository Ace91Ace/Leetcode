# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None and val == 5:
            return TreeNode(5,None,None)
        curr = root
        n = TreeNode(val,None,None)
        while curr:
            if val == curr.val:
                return root
            if val < curr.val:
                if curr.left == None:
                    curr.left = n
                    return root
                curr = curr.left
            else:
                if curr.right == None:
                    curr.right = n
                    return root
                curr = curr.right
