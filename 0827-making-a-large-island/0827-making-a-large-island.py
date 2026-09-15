class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = {}
        island_id = 2  # 从 2 开始,避免跟原始的 0/1 混淆

        # 遍历寻找岛屿面积，并给每一个岛屿进行id:area 编号
        def dfs(i, j, id):
            if not (0 <= i < n and 0 <= j < n):
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = id
            size = 1
            for dx, dy in DIRS:
                size += dfs(i + dx, j + dy, id)
            return size

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[island_id] = dfs(i, j, island_id)
                    island_id += 1

        ans = max(area.values(), default=0)

        for i in range(n):
            for j in range(n):
                # 遍历可以把不同岛屿连接起来的‘0’
                if grid[i][j] == 0:
                    seen = set()
                    total = 1
                    for dx, dy in DIRS:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            id = grid[ni][nj]
                            if id not in seen:
                                seen.add(id)
                                total += area[id]
                    ans = max(ans, total)

        return ans