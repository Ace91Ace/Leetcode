# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head : return None
        if not head.next: return TreeNode(head.val)

        spt , fpt = head, head.next.next

        while fpt and fpt.next:
            fpt = fpt.next.next
            spt = spt.next
        root = TreeNode(spt.next.val)

        rt = spt.next.next
        spt.next = None

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(rt)

        return root
