# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mx_width = 0
        q = deque([(root, 0)])
        while q:
            level_size = len(q)
            _, first_idx = q[0]
            last_idx = first_idx

            for _ in range(level_size):
                node, idx = q.popleft()
                last_idx = idx
                norm_idx = idx - first_idx
                if node.left:
                    q.append((node.left, norm_idx * 2))
                if node.right:
                    q.append((node.right, norm_idx * 2 + 1))

            mx_width = max(mx_width, last_idx - first_idx + 1)

        return mx_width

