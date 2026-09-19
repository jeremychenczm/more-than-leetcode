from collections import defaultdict
class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)

        pos = defaultdict(tuple)
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                pos[val] = (i, j)

        size = n * n
        parent = list(range(size))
        rank = [0] * size
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1

        visited = [[False] * n for _ in range(n)]
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for t in range(size):
            x, y = pos[t]
            visited[x][y] = True
            idx = x * n + y 
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]:
                    union(idx, nx * n + ny)
            if find(0) == find(size - 1):
                return t
        
        return size - 1

        
