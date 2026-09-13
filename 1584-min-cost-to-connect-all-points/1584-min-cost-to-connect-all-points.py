class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        visited = [False] * n

        # 循环n次，每一轮往树里加一个新点
        for _ in range(n):
            # 1. 在未访问的节点里找一个与当前树距离最小min_dist[v]的节点v加入到树中
            u = -1
            for v in range(n):
                if not visited[v] and (u == -1 or min_dist[v] < min_dist[u]):
                    u = v
            visited[u] = True
            ans += min_dist[u]

            # 2. 更新其他未访问节点距离生成树的最小距离
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist

        return ans