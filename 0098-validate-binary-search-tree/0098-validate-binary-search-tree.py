# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        res = []
        def traverse (node):
            if node:
                traverse(node.left)
                res.append(node.val)
                traverse(node.right)
        traverse(root)
        return res

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        x = self.inorder(root)
        y = sorted(x)

        return x==y and len(x) == len(set(x))
        