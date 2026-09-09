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
        ptr = head
        n = 0
        while ptr:
            n += 1
            ptr = ptr.next
        
        self.cur = head
        def build(start, end):
            if start > end:
                return
            mid = (start + end) // 2
            left_subtree = build(start, mid - 1)
            root = TreeNode(self.cur.val)
            root.left = left_subtree
            self.cur = self.cur.next
            root.right = build(mid + 1, end)
            return root
            
        return build(0, n - 1)