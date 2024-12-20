# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def DFS(leftr,rightr,lvl):
            if not leftr or not rightr:
                return
            if lvl % 2 == 0:
                leftr.val , rightr.val = rightr.val,leftr.val
            lvl += 1
            DFS(leftr.left,rightr.right,lvl)
            DFS(leftr.right,rightr.left,lvl)

        DFS(root.left,root.right,0)
        return root