from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 树的最小高度根一定在树的"最长路径"（直径）的中点上，最多两个。
        # 所以核心就是构建一棵树，把叶子一层层去掉，剩下的就是那个root

        if n == 1:
            return [0]

        graph = [[] for _ in range(n)]
        degree = [0] * n
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            degree[x] += 1
            degree[y] += 1

        # 给一个叶子队列，不断的弹掉，直到总数小于2个
        # total 可能为1或2
        leaves = deque(node for node in range(n) if degree[node] == 1)
        total = n  

        # 剥完叶子后最多剩两个
        while total > 2:
            leaves_cnt = len(leaves)
            total -= leaves_cnt
            
            for i in range(leaves_cnt):
                leaf = leaves.popleft()
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    # 如果邻居成为叶子，就加入叶子队列
                    if degree[nei] == 1:
                        leaves.append(nei)

        return list(leaves)
