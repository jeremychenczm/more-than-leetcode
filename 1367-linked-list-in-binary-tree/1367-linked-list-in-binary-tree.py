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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(node, listNode):
            # 如果走到链表末尾，说明路径找到了
            if not listNode:
                return True
            
            if not node or node.val != listNode.val:
                return False
            
            return dfs(node.left, listNode.next) or dfs(node.right, listNode.next)

        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)