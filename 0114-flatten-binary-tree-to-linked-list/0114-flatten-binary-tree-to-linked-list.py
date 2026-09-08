# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left_subtree = root.left
        right_subtree = root.right
        root.left = None
        root.right = left_subtree
        ptr = root
        while ptr.right:
            ptr = ptr.right
        ptr.right = right_subtree