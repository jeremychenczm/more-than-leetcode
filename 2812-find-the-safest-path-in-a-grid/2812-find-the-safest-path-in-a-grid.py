class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        DIRS = {(1, 0), (-1, 0), (0, 1), (0, -1)}

        # 1.从所有小偷出发标记每一个格子距离小偷的距离
        dist = [[-1] * n for _ in range(n)]  # 每一个点位距离小偷的最近距离
        q = []
        for i in range(n):  # 所有小偷入队
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        layers = [q]  # 按层扩散遍历（而非一个个弹出：每一层都有哪些点位
        while q:
            tmp = q
            q = []
            for x, y in tmp:
                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    # dist[nx][ny] < 0 表示第一次访问格子
                    if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] < 0:
                        dist[nx][ny] = len(layers)
                        q.append((nx, ny))
            layers.append(q)


        # 2.利用并查集从最大距离也就是最大安全系数向下开始枚举，看看到哪一层时起点终点连通了
        parent = list(range(n * n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(len(layers) - 2, 0, -1):
            for x, y in layers[i]:
                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    # 当下一层或当前层能够到达，那么(nx, ny)的祖先和当前点位的祖先相同
                    if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] >= i:
                        parent[find(nx * n + ny)] = find(x * n + y)
            if find(0) == find(n * n - 1):
                return i
        
        return 0
