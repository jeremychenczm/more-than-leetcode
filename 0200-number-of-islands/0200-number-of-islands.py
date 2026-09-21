class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.cnt = 0

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.cnt -= 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        # 先统计要处理多少个 ‘1’
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    uf.cnt += 1

        # 进行联通
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    idx = i * n + j
                    if i + 1 < m and grid[i + 1][j] == '1':
                        uf.union(idx, (i + 1) * n + j)
                    if j + 1 < n and grid[i][j + 1] == '1':
                        uf.union(idx, i * n + j + 1)

        return uf.cnt