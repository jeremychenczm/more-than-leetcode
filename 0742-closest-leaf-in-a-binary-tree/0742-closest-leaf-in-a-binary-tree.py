# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        gh = defaultdict(list)
        leaves = set()

        # build graph
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                leaves.add(node.val)
                return
            for child in (node.left, node.right):
                if child:
                    gh[node.val].append(child.val)
                    gh[child.val].append(node.val)
                    dfs(child)
        dfs(root)

        # bfs: start from target K
        visited = {k}
        q = deque([k])
        while q:
            cur = q.popleft()
            if cur in leaves:
                return cur
            for nei in gh[cur]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

